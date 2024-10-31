import os
from neo4j import GraphDatabase
from dotenv import load_dotenv


# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Parâmetros de conexão
uri = os.getenv("NEO4J_URI")
username = os.getenv("NEO4J_USERNAME")
password = os.getenv("NEO4J_PASSWORD")

# Conexão com o banco de dados Neo4j
def connect_to_neo4j(uri, username, password):
    try:
        driver = GraphDatabase.driver(uri, auth=(username, password))
        session = driver.session()
        return session
    except Exception as e:
        print("Erro na conexão com o Neo4j:", e)
        return None

# Função para criar um usuário no banco de dados
def create_user(session, name, age):
    session.run("CREATE (p:User {name: $name, age: $age})", name=name, age=age)
    print(f"Usuário {name} criado com sucesso.")


# Função para listar todos os usuários no banco de dados
def list_people(session):
    result = session.run("MATCH (p:User) RETURN p.name AS name, p.age AS age")
    people = result.values()
    if people:
        print("Lista de usuários:")
        for user in people:
            print(f"Nome: {user[0]}, Idade: {user[1]}")
    else:
        print("Nenhum usuário encontrado.")

# Função para buscar um usuário específico
def read_user(session, name):
    result = session.run("MATCH (p:User {name: $name}) RETURN p.name AS name, p.age AS age", name=name)
    user = result.single()
    if user:
        print(f"Usuário encontrada: Nome: {user['name']}, Idade: {user['age']}")
    else:
        print("Usuário não encontrada.")

# Função para atualizar a idade de uma usuário
def update_user_age(session, name, new_age):
    result = session.run("MATCH (p:User {name: $name}) SET p.age = $new_age RETURN p", name=name, new_age=new_age)
    if result.single():
        print(f"Idade de {name} atualizada para {new_age}.")
    else:
        print("Usuário não encontrada para atualização.")

# Função para deletar um usuário
def delete_user(session, name):
    result = session.run("MATCH (p:User {name: $name}) DELETE p RETURN COUNT(p) AS count", name=name)
    if result.single()["count"] > 0:
        print(f"Usuário {name} deletada com sucesso.")
    else:
        print("Usuário não encontrada para deletar.")

# Função para criar relacionamento de amizade entre dois usuários
def create_friendship(session, name1, name2):
    result = session.run(
        """
        MATCH (p1:user {name: $name1}), (p2:user {name: $name2})
        CREATE (p1)-[:AMIGO]->(p2)
        RETURN p1, p2
        """, name1=name1, name2=name2)
    
    if result.single():
        print(f"Relacionamento de amizade criado entre os usuários {name1} e {name2}.")
    else:
        print("Um ou ambos os usuários não foram encontrados.")

# Função para deletar todos usuários
def delete_all_people(session):
    session.run("MATCH (p:User) DETACH DELETE p")
    print("Todas os usuários deletados com sucesso.")

# Função para mostrar o menu e capturar a escolha do usuário
def show_menu():
    print("\nEscolha uma opção:")
    print("1. Buscar usuário")
    print("2. Adicionar novo usuário")
    print("3. Listar todos usuários")
    print("4. Criar relacionamento de amizade")
    print("5. Atualizar idade de usuário")
    print("6. Deletar usuário")
    print("7. Deletar todos os usuários")
    print("8. Sair")
    return input("Digite o número da opção: ")


# Tentar conectar ao banco de dados
session = connect_to_neo4j(uri, username, password)

# Executar operações de CRUD com interação no terminal
if session:
    print("Conexão com o Neo4j estabelecida com sucesso!")
    
    while True:
        opcao = show_menu()
        
        if opcao == "1":
            name = input("Digite o nome do usuário para buscar: ")
            read_user(session, name)
                
        elif opcao == "2":
            name = input("Digite o nome do usuário: ")
            age = int(input("Digite a idade do usuário: "))
            create_user(session, name, age)
        
        elif opcao == "3":
            list_people(session)
        
        elif opcao == "4":
            name1 = input("Digite o nome do primeiro usuário: ")
            name2 = input("Digite o nome do segundo usuário: ")
            create_friendship(session, name1, name2)
        
        elif opcao == "5":
            name = input("Digite o nome do usuário para atualizar: ")
            new_age = int(input("Digite a nova idade: "))
            update_user_age(session, name, new_age)
        
        elif opcao == "6":
            name = input("Digite o nome do usuário para deletar: ")
            delete_user(session, name)
        
        elif opcao == "7":
            confirm = input("Tem certeza de que deseja deletar todas as pessoas? (s/n): ")
            if confirm.lower() == "s":
                delete_all_people(session)
            else:
                print("Operação cancelada.")
        
        elif opcao == "8":
            print("Encerrando o programa.")
            break
        
        else:
            print("Opção inválida. Tente novamente.")
    
    session.close()  # Fechar a sessão
else:
    print("Não foi possível estabelecer conexão com o Neo4j.")
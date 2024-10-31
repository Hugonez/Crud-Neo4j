Este é um projeto simples de CRUD (Create, Read, Update, Delete) para gerenciar usuários e criar relacionamentos de amizade entre eles em um banco de dados Neo4j. A aplicação interage com o usuário via terminal, permitindo adicionar, listar, buscar, atualizar, deletar usuários e criar relacionamentos entre eles.

## Pré-requisitos

- Python 3.x
- Biblioteca `neo4j`
- Biblioteca `python-dotenv` para carregar variáveis de ambiente
- Banco de dados Neo4j em execução

## Configuração
# 1. Clone o repositório
git clone https://github.com/seu_usuario/neo4j-crud.git
cd neo4j-crud

# 2. Instale as dependências
pip install neo4j python-dotenv

# 3. Crie o arquivo .env na raiz do projeto com as variáveis de conexão:
echo -e "NEO4J_URI=bolt://localhost:7687\nNEO4J_USERNAME=Hugonez\nNEO4J_PASSWORD=sua_senha" > .env

## Estrutura do Código
 connect_to_neo4j:   conecta ao banco Neo4j utilizando credenciais do .env.
 create_user:  cria um novo usuário com nome e idade especificados.
 list_user: lista todos os usuários cadastrados.
 read_user:  busca um usuário específico pelo nome.
 update_user_age: atualiza a idade de um usuário.
 delete_user: deleta um usuário específico.
 create_friendship: cria uma relação de amizade entre dois usuários.
 delete_all_user: deleta todos os usuários cadastrados.

## Como Usar
  Execute o script com o comando:
    `python nome_do_arquivo.py`
    
  Navegue pelo Menu Interativo para realizar operações como adicionar, listar, atualizar e deletar usuários, além de criar relações de amizade entre eles.
  
  Escolha uma opção do menu de 1 a 8 para executar uma operação.

## Exemplo de Uso
  Para adicionar um usuário  selecione a opção 2 e insira o nome e a idade do usuário.
  Para listar todos os usuários escolha a opção 3.
  Para atualizar a idade de um usuário escolha a opção 5 e insira o nome do usuário e a nova idade.
  Para deletar todos os usuários escolha a opção 7 e confirme a ação.

## Observações
Certifique-se de que o Neo4j esteja em execução e que as credenciais no arquivo .env estejam corretas.

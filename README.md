# API Salão de Beleza

API desenvolvida para a disciplina de Projeto e Desenvolvimento de Software.

## Integrantes

- Lucas Emanuel da Silva Costa
- Ysabell Vaneires Ferreira Souza

## Tecnologias utilizadas

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn

## Funcionalidades

- Cadastro de usuários
- Cadastro de clientes
- Cadastro de serviços
- Cadastro de agendamentos
- Consulta de registros
- Proteção de endpoints com API Key
- Armazenamento seguro de senhas utilizando Hash

## Padrões de Projeto

- Singleton
- Factory

## Banco de Dados

- SQLite utilizando ORM com SQLAlchemy.

## Como executar

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
````
## A documentação da API pode ser acessada em:

```bash
http://127.0.0.1:8000/docs
````

#ALUNOS: Lucas Emanuel da Silva Costa e Ysabell Vaneires Souza
from hash import gerar_hash
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from security import verificar_api_key
from fastapi import Depends
from factory import UsuarioFactory, ClienteFactory, AgendamentoFactory

from database import SessionLocal, engine, Base

import models

from schemas import *

Base.metadata.create_all(bind=engine)
def get_db():

    db = SessionLocal()

    try:

        yield db

    finally:

        db.close()


app = FastAPI(title="Sistema de Gerenciamento para Salão de Beleza")

# MODELOS 


class Usuario(BaseModel):
    id: int
    nome: str
    email: str
    senha: str
    cargo: str

class Servico(BaseModel):
    id: int
    nome: str
    preco: float
    duracao: int
    ativo: bool = True


usuarios = []
servicos = []


# CRUD USUÁRIOS

# ==========================
# CRUD USUÁRIOS (ORM)
# ==========================

@app.post(
    "/usuarios",
    response_model=UsuarioSaida,
    dependencies=[Depends(verificar_api_key)]
)
def criar_usuario(
    usuario: UsuarioEntrada,
    db: Session = Depends(get_db)
):

    senha_hash = gerar_hash(usuario.senha)

    novo = UsuarioFactory.criar(usuario)

    db.add(novo)

    db.commit()

    db.refresh(novo)

    return novo


@app.get("/usuarios", response_model=list[UsuarioSaida])
def listar_usuarios(db: Session = Depends(get_db)):

    return db.query(models.Usuario).all()


@app.get("/usuarios/{id}", response_model=UsuarioSaida)
def buscar_usuario(
    id: int,
    db: Session = Depends(get_db)
):

    usuario = db.query(models.Usuario).filter(
        models.Usuario.id == id
    ).first()

    if not usuario:

        raise HTTPException(
            status_code=404,
            detail="Usuário não encontrado"
        )

    return usuario


@app.put(
    "/usuarios/{id}",
    response_model=UsuarioSaida,
    dependencies=[Depends(verificar_api_key)]
)
def atualizar_usuario(
    id: int,
    dados: UsuarioEntrada,
    db: Session = Depends(get_db)
):

    usuario = db.query(models.Usuario).filter(
        models.Usuario.id == id
    ).first()

    if not usuario:

        raise HTTPException(
            status_code=404,
            detail="Usuário não encontrado"
        )

    usuario.nome = dados.nome
    usuario.email = dados.email
    usuario.cargo = dados.cargo
    usuario.senha = gerar_hash(dados.senha)

    db.commit()

    db.refresh(usuario)

    return usuario


@app.delete(
    "/usuarios/{id}",
    dependencies=[Depends(verificar_api_key)]
)
def remover_usuario(
    id: int,
    db: Session = Depends(get_db)
):

    usuario = db.query(models.Usuario).filter(
        models.Usuario.id == id
    ).first()

    if not usuario:

        raise HTTPException(
            status_code=404,
            detail="Usuário não encontrado"
        )

    db.delete(usuario)

    db.commit()

    return {"mensagem": "Usuário removido"}

# CRUD CLIENTES

@app.post(
    "/clientes",
    response_model=ClienteSaida,
    dependencies=[Depends(verificar_api_key)]
)
def criar_cliente(cliente: ClienteEntrada, db: Session = Depends(get_db)):

    novo = ClienteFactory.criar(cliente)

    db.add(novo)

    db.commit()

    db.refresh(novo)

    return novo


@app.get("/clientes", response_model=list[ClienteSaida])

def listar_clientes(db: Session = Depends(get_db)):

    return db.query(models.Cliente).all()


@app.get("/clientes/{id}", response_model=ClienteSaida)

def buscar_cliente(id: int, db: Session = Depends(get_db)):

    cliente = db.query(models.Cliente).filter(models.Cliente.id == id).first()

    if not cliente:

        raise HTTPException(404, "Cliente não encontrado")

    return cliente


@app.put(
    "/clientes/{id}",
    response_model=ClienteSaida,
    dependencies=[Depends(verificar_api_key)]
)
def atualizar_cliente(id: int,
                      dados: ClienteEntrada,
                      db: Session = Depends(get_db)):

    cliente = db.query(models.Cliente).filter(models.Cliente.id == id).first()

    if not cliente:

        raise HTTPException(404, "Cliente não encontrado")

    cliente.nome = dados.nome

    cliente.telefone = dados.telefone

    cliente.email = dados.email

    db.commit()

    db.refresh(cliente)

    return cliente


@app.delete(
    "/clientes/{id}",
    dependencies=[Depends(verificar_api_key)]
)
def remover_cliente(id: int, db: Session = Depends(get_db)):

    cliente = db.query(models.Cliente).filter(models.Cliente.id == id).first()

    if not cliente:

        raise HTTPException(404, "Cliente não encontrado")

    db.delete(cliente)

    db.commit()

    return {"mensagem":"Cliente removido"}

# CRUD SERVIÇOS

@app.post("/servicos")
def criar_servico(servico: Servico):
    servicos.append(servico)
    return servico


@app.get("/servicos")
def listar_servicos():
    return servicos


@app.get("/servicos/{servico_id}")
def buscar_servico(servico_id: int):
    for servico in servicos:
        if servico.id == servico_id:
            return servico
    raise HTTPException(status_code=404, detail="Serviço não encontrado")


@app.put("/servicos/{servico_id}")
def atualizar_servico(servico_id: int, servico_atualizado: Servico):
    for i, servico in enumerate(servicos):
        if servico.id == servico_id:
            servicos[i] = servico_atualizado
            return servico_atualizado
    raise HTTPException(status_code=404, detail="Serviço não encontrado")


@app.delete("/servicos/{servico_id}")
def remover_servico(servico_id: int):
    for servico in servicos:
        if servico.id == servico_id:
            servicos.remove(servico)
            return {"mensagem": "Serviço removido"}
    raise HTTPException(status_code=404, detail="Serviço não encontrado")


# CRUD AGENDAMENTOS (ORM)

@app.post(
    "/agendamentos",
    response_model=AgendamentoSaida,
    dependencies=[Depends(verificar_api_key)]
)

def criar_agendamento(
    agendamento: AgendamentoEntrada,
    db: Session = Depends(get_db)
):
    novo = AgendamentoFactory.criar(agendamento)

    db.add(novo)
    db.commit()
    db.refresh(novo)

    return novo


@app.get("/agendamentos", response_model=list[AgendamentoSaida])
def listar_agendamentos(db: Session = Depends(get_db)):
    return db.query(models.Agendamento).all()


@app.get("/agendamentos/{id}", response_model=AgendamentoSaida)
def buscar_agendamento(id: int, db: Session = Depends(get_db)):

    agendamento = (
        db.query(models.Agendamento)
        .filter(models.Agendamento.id == id)
        .first()
    )

    if not agendamento:
        raise HTTPException(status_code=404, detail="Agendamento não encontrado")

    return agendamento


@app.put(
    "/agendamentos/{id}",
    response_model=AgendamentoSaida,
    dependencies=[Depends(verificar_api_key)]
)
def atualizar_agendamento(
    id: int,
    dados: AgendamentoEntrada,
    db: Session = Depends(get_db)
):

    agendamento = (
        db.query(models.Agendamento)
        .filter(models.Agendamento.id == id)
        .first()
    )

    if not agendamento:
        raise HTTPException(status_code=404, detail="Agendamento não encontrado")

    agendamento.cliente_id = dados.cliente_id
    agendamento.usuario_id = dados.usuario_id
    agendamento.servico_id = dados.servico_id
    agendamento.data = dados.data
    agendamento.horario = dados.horario
    agendamento.status = dados.status

    db.commit()
    db.refresh(agendamento)

    return agendamento


@app.delete(
    "/agendamentos/{id}",
    dependencies=[Depends(verificar_api_key)]
)
def remover_agendamento(
    id: int,
    db: Session = Depends(get_db)
):
    agendamento = (
        db.query(models.Agendamento)
        .filter(models.Agendamento.id == id)
        .first()
    )

    if not agendamento:
        raise HTTPException(status_code=404, detail="Agendamento não encontrado")

    db.delete(agendamento)
    db.commit()

    return {"mensagem": "Agendamento removido"}

# RELACIONAMENTOS

@app.get("/clientes/{cliente_id}/agendamentos")
def listar_agendamentos_cliente(
    cliente_id: int,
    db: Session = Depends(get_db)
):

    return (
        db.query(models.Agendamento)
        .filter(models.Agendamento.cliente_id == cliente_id)
        .all()
    )


# @app.get("/usuarios/{usuario_id}/agendamentos")
# def listar_agendamentos_usuario(usuario_id: int):
#     return [a for a in agendamentos if a.usuario_id == usuario_id]


# @app.get("/servicos/{servico_id}/agendamentos")
# def listar_agendamentos_servico(servico_id: int):
#     return [a for a in agendamentos if a.servico_id == servico_id]


@app.get("/agendamentos/data/{data}")
def listar_agendamentos_por_data(
    data: str,
    db: Session = Depends(get_db)
):

    return (
        db.query(models.Agendamento)
        .filter(models.Agendamento.data == data)
        .all()
    )
#ALUNOS: Lucas Emanuel da Silva Costa e Ysabell Vaneires Souza

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Sistema de Gerenciamento para Salão de Beleza")

# MODELOS 

class Usuario(BaseModel):
    id: int
    nome: str
    email: str
    senha: str
    cargo: str


class Cliente(BaseModel):
    id: int
    nome: str
    telefone: str
    email: str


class Servico(BaseModel):
    id: int
    nome: str
    preco: float
    duracao: int
    ativo: bool = True


class Agendamento(BaseModel):
    id: int
    cliente_id: int
    servico_id: int
    usuario_id: int
    data: str
    horario: str
    status: str


usuarios = []
clientes = []
servicos = []
agendamentos = []


# CRUD USUÁRIOS

@app.post("/usuarios")
def criar_usuario(usuario: Usuario):
    usuarios.append(usuario)
    return usuario


@app.get("/usuarios")
def listar_usuarios():
    return usuarios


@app.get("/usuarios/{usuario_id}")
def buscar_usuario(usuario_id: int):
    for usuario in usuarios:
        if usuario.id == usuario_id:
            return usuario
    raise HTTPException(status_code=404, detail="Usuário não encontrado")


@app.put("/usuarios/{usuario_id}")
def atualizar_usuario(usuario_id: int, usuario_atualizado: Usuario):
    for i, usuario in enumerate(usuarios):
        if usuario.id == usuario_id:
            usuarios[i] = usuario_atualizado
            return usuario_atualizado
    raise HTTPException(status_code=404, detail="Usuário não encontrado")


@app.delete("/usuarios/{usuario_id}")
def remover_usuario(usuario_id: int):
    for usuario in usuarios:
        if usuario.id == usuario_id:
            usuarios.remove(usuario)
            return {"mensagem": "Usuário removido"}
    raise HTTPException(status_code=404, detail="Usuário não encontrado")


# CRUD CLIENTES

@app.post("/clientes")
def criar_cliente(cliente: Cliente):
    clientes.append(cliente)
    return cliente


@app.get("/clientes")
def listar_clientes():
    return clientes


@app.get("/clientes/{cliente_id}")
def buscar_cliente(cliente_id: int):
    for cliente in clientes:
        if cliente.id == cliente_id:
            return cliente
    raise HTTPException(status_code=404, detail="Cliente não encontrado")


@app.put("/clientes/{cliente_id}")
def atualizar_cliente(cliente_id: int, cliente_atualizado: Cliente):
    for i, cliente in enumerate(clientes):
        if cliente.id == cliente_id:
            
            clientes[i] = cliente_atualizado
            return cliente_atualizado
    raise HTTPException(status_code=404, detail="Cliente não encontrado")


@app.delete("/clientes/{cliente_id}")
def remover_cliente(cliente_id: int):
    for cliente in clientes:
        if cliente.id == cliente_id:
            clientes.remove(cliente)
            return {"mensagem": "Cliente removido"}
    raise HTTPException(status_code=404, detail="Cliente não encontrado")


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


# CRUD AGENDAMENTOS

@app.post("/agendamentos")
def criar_agendamento(agendamento: Agendamento):
    agendamentos.append(agendamento)
    return agendamento


@app.get("/agendamentos")
def listar_agendamentos():
    return agendamentos


@app.get("/agendamentos/{agendamento_id}")
def buscar_agendamento(agendamento_id: int):
    for agendamento in agendamentos:
        if agendamento.id == agendamento_id:
            return agendamento
    raise HTTPException(status_code=404, detail="Agendamento não encontrado")


@app.put("/agendamentos/{agendamento_id}")
def atualizar_agendamento(agendamento_id: int, agendamento_atualizado: Agendamento):
    for i, agendamento in enumerate(agendamentos):
        if agendamento.id == agendamento_id:
            agendamentos[i] = agendamento_atualizado
            return agendamento_atualizado
    raise HTTPException(status_code=404, detail="Agendamento não encontrado")


@app.delete("/agendamentos/{agendamento_id}")
def remover_agendamento(agendamento_id: int):
    for agendamento in agendamentos:
        if agendamento.id == agendamento_id:
            agendamentos.remove(agendamento)
            return {"mensagem": "Agendamento removido"}
    raise HTTPException(status_code=404, detail="Agendamento não encontrado")


# RELACIONAMENTOS

@app.get("/clientes/{cliente_id}/agendamentos")
def listar_agendamentos_cliente(cliente_id: int):
    return [a for a in agendamentos if a.cliente_id == cliente_id]


@app.get("/usuarios/{usuario_id}/agendamentos")
def listar_agendamentos_usuario(usuario_id: int):
    return [a for a in agendamentos if a.usuario_id == usuario_id]


@app.get("/servicos/{servico_id}/agendamentos")
def listar_agendamentos_servico(servico_id: int):
    return [a for a in agendamentos if a.servico_id == servico_id]


@app.get("/agendamentos/data/{data}")
def listar_agendamentos_por_data(data: str):
    return [a for a in agendamentos if a.data == data]
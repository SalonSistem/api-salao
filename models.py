from pydantic import BaseModel

# USUÁRIOS

class UsuarioEntrada(BaseModel):
    nome: str
    email: str
    senha: str
    cargo: str


class Usuario(UsuarioEntrada):
    id: int

# CLIENTES

class ClienteEntrada(BaseModel):
    nome: str
    telefone: str
    email: str


class Cliente(ClienteEntrada):
    id: int

# SERVIÇOS

class ServicoEntrada(BaseModel):
    nome: str
    preco: float
    duracao: int
    ativo: bool


class Servico(ServicoEntrada):
    id: int

# AGENDAMENTOS

class AgendamentoEntrada(BaseModel):
    cliente_id: int
    usuario_id: int
    servico_id: int
    data: str
    horario: str
    status: str


class Agendamento(AgendamentoEntrada):
    id: int
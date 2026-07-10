from pydantic import BaseModel

# ---------- Usuários ----------

class UsuarioBase(BaseModel):
    nome: str
    email: str
    senha: str
    cargo: str


class UsuarioCreate(UsuarioBase):
    pass


class Usuario(UsuarioBase):
    id: int

    class Config:
        from_attributes = True


# ---------- Clientes ----------

class ClienteBase(BaseModel):
    nome: str
    telefone: str
    email: str


class ClienteCreate(ClienteBase):
    pass


class Cliente(ClienteBase):
    id: int

    class Config:
        from_attributes = True


# ---------- Serviços ----------

class ServicoBase(BaseModel):
    nome: str
    preco: float
    duracao: int
    ativo: bool


class ServicoCreate(ServicoBase):
    pass


class Servico(ServicoBase):
    id: int

    class Config:
        from_attributes = True


# ---------- Agendamentos ----------

class AgendamentoBase(BaseModel):
    cliente_id: int
    usuario_id: int
    servico_id: int
    data: str
    horario: str
    status: str


class AgendamentoCreate(AgendamentoBase):
    pass


class Agendamento(AgendamentoBase):
    id: int

    class Config:
        from_attributes = True
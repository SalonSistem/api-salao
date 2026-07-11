from pydantic import BaseModel

class UsuarioEntrada(BaseModel):
    nome: str
    email: str
    senha: str
    cargo: str


class UsuarioSaida(BaseModel):
    id: int
    nome: str
    email: str
    cargo: str

    class Config:
        from_attributes = True

class ClienteEntrada(BaseModel):
    nome: str
    telefone: str
    email: str


class ClienteSaida(ClienteEntrada):
    id: int

    class Config:
        from_attributes = True


class AgendamentoEntrada(BaseModel):
    cliente_id: int
    usuario_id: int
    servico_id: int
    data: str
    horario: str
    status: str


class AgendamentoSaida(AgendamentoEntrada):
    id: int

    class Config:
        from_attributes = True
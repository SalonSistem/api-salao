from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base

class Usuario(Base):

    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)

    nome = Column(String, nullable=False)

    email = Column(String, nullable=False, unique=True)

    senha = Column(String, nullable=False)

    cargo = Column(String, nullable=False)
    
class Cliente(Base):

    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)

    nome = Column(String, nullable=False)

    telefone = Column(String, nullable=False)

    email = Column(String, nullable=False)

    agendamentos = relationship("Agendamento", back_populates="cliente")

class Agendamento(Base):

    __tablename__ = "agendamentos"

    id = Column(Integer, primary_key=True, index=True)

    cliente_id = Column(Integer, ForeignKey("clientes.id"), nullable=False)

    usuario_id = Column(Integer, nullable=False)

    servico_id = Column(Integer, nullable=False)

    data = Column(String, nullable=False)

    horario = Column(String, nullable=False)

    status = Column(String, nullable=False)

    cliente = relationship("Cliente", back_populates="agendamentos")
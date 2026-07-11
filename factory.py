import models
from hash import gerar_hash


class UsuarioFactory:

    @staticmethod
    def criar(usuario):

        return models.Usuario(
            nome=usuario.nome,
            email=usuario.email,
            senha=gerar_hash(usuario.senha),
            cargo=usuario.cargo
        )


class ClienteFactory:

    @staticmethod
    def criar(cliente):

        return models.Cliente(
            nome=cliente.nome,
            telefone=cliente.telefone,
            email=cliente.email
        )


class AgendamentoFactory:

    @staticmethod
    def criar(agendamento):

        return models.Agendamento(
            cliente_id=agendamento.cliente_id,
            usuario_id=agendamento.usuario_id,
            servico_id=agendamento.servico_id,
            data=agendamento.data,
            horario=agendamento.horario,
            status=agendamento.status
        )
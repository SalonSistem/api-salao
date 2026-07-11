class ConfigBanco:

    _instancia = None

    def __new__(cls):

        if cls._instancia is None:

            cls._instancia = super().__new__(cls)

            cls._instancia.nome = "salao.db"

        return cls._instancia
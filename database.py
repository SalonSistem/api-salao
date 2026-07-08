import sqlite3

DB_PATH = "salao.db"

def get_conn() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def init_db():
    with get_conn() as conn:
        conn.executescript("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id      INTEGER PRIMARY KEY AUTOINCREMENT,
                nome    TEXT NOT NULL,
                email   TEXT NOT NULL UNIQUE,
                senha   TEXT NOT NULL,
                cargo   TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS clientes (
                id        INTEGER PRIMARY KEY AUTOINCREMENT,
                nome      TEXT NOT NULL,
                telefone  TEXT NOT NULL,
                email     TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS servicos (
                id        INTEGER PRIMARY KEY AUTOINCREMENT,
                nome      TEXT NOT NULL,
                preco     REAL NOT NULL,
                duracao   INTEGER NOT NULL,
                ativo     INTEGER NOT NULL
            );

            CREATE TABLE IF NOT EXISTS agendamentos (
                id           INTEGER PRIMARY KEY AUTOINCREMENT,
                cliente_id   INTEGER NOT NULL,
                usuario_id   INTEGER NOT NULL,
                servico_id   INTEGER NOT NULL,
                data         TEXT NOT NULL,
                horario      TEXT NOT NULL,
                status       TEXT NOT NULL,

                FOREIGN KEY (cliente_id) REFERENCES clientes(id),
                FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
                FOREIGN KEY (servico_id) REFERENCES servicos(id)
            );
        """)
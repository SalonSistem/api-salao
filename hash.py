import hashlib

def gerar_hash(senha: str):
    return hashlib.sha256(senha.encode()).hexdigest()

def verificar_senha(senha: str, hash_salvo: str):
    return gerar_hash(senha) == hash_salvo
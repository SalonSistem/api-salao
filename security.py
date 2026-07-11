from fastapi import Header, HTTPException

API_KEY = "api-salao-2026"


def verificar_api_key(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(
            status_code=401,
            detail="API Key inválida"
        )
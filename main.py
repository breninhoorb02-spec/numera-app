from fastapi import FastAPI, HTTPException
from auth_banco import gerar_token
from models import Extrato

app = FastAPI(title="Numera Open Finance Backend")

# Teste simples
@app.get("/ping")
def ping():
    return {"status": "ok"}

# Receber extrato do cliente
@app.post("/extrato")
def receber_extrato(extrato: Extrato):
    try:
        # Aqui você pode salvar no banco ou processar
        # Exemplo: salvar em CSV ou enviar para Streamlit
        # extrato.dict() → contém todos os dados
        return {"status": "recebido", "total_movimentacoes": len(extrato.movimentacoes)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Gerar token Belvo
@app.get("/token")
def token():
    try:
        t = gerar_token()
        return {"token": t}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

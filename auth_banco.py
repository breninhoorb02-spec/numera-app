import requests
import os

# Exemplo Belvo
BELVO_BASE = "https://api.belvo.com"
BELVO_SECRET = os.getenv("BELVO_SECRET")
BELVO_KEY = os.getenv("BELVO_KEY")

def gerar_token():
    resp = requests.post(
        f"{BELVO_BASE}/api/token/",
        auth=(BELVO_KEY, BELVO_SECRET)
    )
    if resp.status_code == 200:
        return resp.json().get("access_token")
    else:
        raise Exception("Erro ao gerar token Belvo")

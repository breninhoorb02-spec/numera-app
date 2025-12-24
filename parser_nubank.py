
import pdfplumber
import pandas as pd

def extrair_nubank(file):
    dados = []

    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            texto = page.extract_text()
            if not texto:
                continue

            for linha in texto.split("\n"):
                partes = linha.split()
                if len(partes) >= 3 and "/" in partes[0]:
                    try:
                        dados.append({
                            "Data": partes[0],
                            "Descrição": " ".join(partes[1:-1]),
                            "Valor": float(partes[-1].replace(",", "").replace("R$", ""))
                        })
                    except:
                        pass

    return pd.DataFrame(dados)

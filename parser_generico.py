import pdfplumber
import pandas as pd
import re

def extrair_pdf_generico(file):
    dados = []

    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            texto = page.extract_text()
            if not texto:
                continue

            for linha in texto.split("\n"):
                match = re.search(r'(\d{2}/\d{2}/\d{4}).+?([\d,]+\.\d{2})', linha)
                if match:
                    data = match.group(1)
                    valor = match.group(2).replace(",", "")
                    dados.append({
                        "Data": data,
                        "Descrição": linha,
                        "Valor": float(valor)
                    })

    return pd.DataFrame(dados)

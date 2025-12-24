import pdfplumber
import pandas as pd
import re

def extrair_caixa(file):
    dados = []

    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            texto = page.extract_text()
            if not texto:
                continue

            for linha in texto.split("\n"):
                match = re.search(
                    r'(\d{2}/\d{2}/\d{4})\s+(.*?)\s+([0-9.,-]+)',
                    linha
                )
                if match:
                    dados.append({
                        "Data": match.group(1),
                        "Descrição": match.group(2),
                        "Valor": float(match.group(3).replace(".", "").replace(",", "."))
                    })

    return pd.DataFrame(dados)

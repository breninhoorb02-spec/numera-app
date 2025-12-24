import re
import pandas as pd

def extrair_nubank(texto):
    linhas = texto.split("\n")
    registros = []

    for linha in linhas:
        if "R$" in linha:
            valor = re.findall(r"-?\d+,\d{2}", linha)
            data = re.findall(r"\d{2}/\d{2}/\d{4}", linha)

            if valor:
                registros.append({
                    "Data": data[0] if data else "",
                    "Descrição": linha,
                    "Valor": valor[0]
                })

    df = pd.DataFrame(registros)

    if not df.empty:
        df["Valor"] = (
            df["Valor"]
            .str.replace(",", ".", regex=False)
            .astype(float)
        )

    return df

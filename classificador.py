def classificar(descricao, valor):
    desc = descricao.lower()

    if valor > 0:
        return "Receita"

    if any(p in desc for p in ["aluguel", "energia", "agua", "internet"]):
        return "Despesa Fixa"

    if any(p in desc for p in ["uber", "99", "combustivel"]):
        return "Despesa Transporte"

    if any(p in desc for p in ["pix", "transferencia"]):
        return "Transferência"

    return "Outros"

def classificar(descricao, valor):
    desc = descricao.lower()

    # RECEITAS
    if valor > 0:
        if any(p in desc for p in ["pix", "credito", "recebimento", "venda"]):
            return "Receita Operacional"
        return "Outras Receitas"

    # DESPESAS FIXAS
    if any(p in desc for p in [
        "aluguel", "energia", "água", "internet",
        "telefone", "condominio"
    ]):
        return "Despesa Fixa"

    # DESPESAS OPERACIONAIS
    if any(p in desc for p in [
        "uber", "99", "combustivel", "posto",
        "manutenção", "frete", "logistica"
    ]):
        return "Despesa Operacional"

    # IMPOSTOS
    if any(p in desc for p in [
        "simples", "das", "iss", "icms", "inss"
    ]):
        return "Impostos"

    # TRANSFERÊNCIAS
    if any(p in desc for p in [
        "pix", "transferencia", "ted", "doc"
    ]):
        return "Transferência"

    return "Outras Despesas"

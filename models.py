from pydantic import BaseModel
from typing import List

class Movimentacao(BaseModel):
    data: str
    descricao: str
    valor: float
    categoria: str

class Extrato(BaseModel):
    banco: str
    cpf_cnpj: str
    movimentacoes: List[Movimentacao]

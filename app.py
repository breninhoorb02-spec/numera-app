import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="NUMERA • Inteligência Financeira",
    layout="centered"
)

st.title("📊 NUMERA • Inteligência Financeira")
st.subheader("Plataforma de Análise Financeira, Contábil e de Vendas")

st.markdown("---")

st.header("📁 Envie seus arquivos")

vendas_file = st.file_uploader("Planilha de Vendas (Excel)", type=["xlsx"])
financeiro_file = st.file_uploader("Planilha Financeira (Excel)", type=["xlsx"])

if vendas_file and financeiro_file:
    vendas = pd.read_excel(vendas_file)
    financeiro = pd.read_excel(financeiro_file)

    faturamento = vendas["Valor"].sum()
    ticket_medio = vendas["Valor"].mean()
    despesas = financeiro["Valor"].sum()
    resultado = faturamento - despesas

    st.markdown("---")
    st.header("📈 Resultado da Análise")

    st.metric("Faturamento Total", f"R$ {faturamento:,.2f}")
    st.metric("Ticket Médio", f"R$ {ticket_medio:,.2f}")
    st.metric("Despesas Totais", f"R$ {despesas:,.2f}")
    st.metric("Lucro / Prejuízo", f"R$ {resultado:,.2f}")

    st.markdown("---")
    st.subheader("🧠 Análise Inteligente")

    if resultado > 0:
        st.success("Sua empresa está lucrando. Avalie reinvestir no crescimento.")
    else:
        st.error("Atenção: despesas maiores que o faturamento. Reveja custos.")

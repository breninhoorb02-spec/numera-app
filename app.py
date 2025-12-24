import streamlit as st
from auth import login
from landing import show_landing
from planos import verificar_plano, mostrar_upgrade, pode_usar, registrar_uso

from parser_nubank import extrair_nubank
from parser_generico import extrair_pdf_generico
from parser_bb import extrair_bb
from parser_bradesco import extrair_bradesco
from parser_caixa import extrair_caixa

from classificador import classificar

st.set_page_config(
    page_title="NUMERA FREE • Teste",
    layout="centered"
)

if not login():
    st.stop()

menu = st.sidebar.radio(
    "Menu",
    ["Início", "Conciliação Bancária"]
)

if menu == "Início":
    st.title("NUMERA FREE")
    st.markdown("Plataforma gratuita de teste. Limite: 1 PDF por usuário.")
    show_landing()

elif menu == "Conciliação Bancária":
    if not pode_usar():
        mostrar_upgrade()
        st.stop()

    st.subheader("🏦 Conciliação PDF")
    banco = st.selectbox(
        "Banco",
        ["Nubank", "Banco do Brasil", "Bradesco", "Caixa Econômica", "Outro banco"]
    )
    arquivo = st.file_uploader("Envie o extrato bancário (PDF)", type=["pdf"])

    if arquivo:
        with st.spinner("Processando PDF..."):
            try:
                if banco == "Nubank":
                    df = extrair_nubank(arquivo)
                elif banco == "Banco do Brasil":
                    df = extrair_bb(arquivo)
                elif banco == "Bradesco":
                    df = extrair_bradesco(arquivo)
                elif banco == "Caixa Econômica":
                    df = extrair_caixa(arquivo)
                else:
                    df = extrair_pdf_generico(arquivo)

                if df.empty:
                    st.warning("Nenhuma movimentação encontrada.")
                else:
                    df["Categoria"] = df.apply(lambda x: classificar(x["Descrição"], x["Valor"]), axis=1)
                    registrar_uso()
                    st.success("Conciliação concluída")
                    st.dataframe(df)
                    st.download_button(
                        "⬇️ Baixar CSV classificado",
                        df.to_csv(index=False),
                        file_name="numera_lancamentos_free.csv",
                        mime="text/csv"
                    )
            except Exception as e:
                st.error("Erro ao processar PDF")
                st.exception(e)

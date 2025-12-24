import streamlit as st
from auth import login
from landing import show_landing
from planos import verificar_plano, mostrar_upgrade
from parser_generico import extrair_pdf_generico
from parser_nubank import extrair_nubank

st.set_page_config(
    page_title="NUMERA • Inteligência Financeira",
    layout="centered"
)

# 🔐 LOGIN
if not login():
    st.stop()

# 📌 MENU LATERAL
menu = st.sidebar.radio(
    "Menu",
    ["Início", "Conciliação Bancária", "Planos"]
)

# 🏠 INÍCIO
if menu == "Início":
    show_landing()

# 💳 PLANOS
elif menu == "Planos":
    plano = verificar_plano()
    st.subheader("💳 Seu plano")
    st.info(f"Plano atual: {plano}")

# 🏦 CONCILIAÇÃO
elif menu == "Conciliação Bancária":

    plano = verificar_plano()

    if plano == "free":
        mostrar_upgrade()
        st.stop()

    st.subheader("🏦 Conciliação Bancária por PDF")

    banco = st.selectbox(
        "Selecione o banco",
        [
            "Nubank",
            "Banco do Brasil",
            "Bradesco",
            "Caixa Econômica",
            "Outro banco"
        ]
    )

    arquivo = st.file_uploader(
        "Envie o extrato bancário (PDF)",
        type=["pdf"]
    )

    if arquivo:
        with st.spinner("🔄 Processando extrato..."):
            try:
                if banco == "Nubank":
                    df = extrair_nubank(arquivo)
                else:
                    df = extrair_pdf_generico(arquivo)

                if df.empty:
                    st.warning("Nenhuma movimentação encontrada no PDF.")
                else:
                    st.success("✅ Conciliação realizada com sucesso")
                    st.dataframe(df)

                    st.download_button()
                        "⬇️ Baixar lançamentos (CSV)",
                        df.to_csv(index=False),
                        file_name="lancamentos_numera.csv",
                        mime="text/csv"
                        df["Categoria"] = df.apply(
    lambda x: classificar(x["Descrição"], x["Valor"]), axis=1
                    
                    )

            except Exception as e:
                st.error("❌ Erro ao processar o extrato")
                st.exception(e)

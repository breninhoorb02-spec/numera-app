import streamlit as st
import requests
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
    page_title="NUMERA • Inteligência Financeira",
    layout="centered"
)

# 🔐 LOGIN
if not login():
    st.stop()

menu = st.sidebar.radio(
    "Menu",
    ["Início", "Conciliação Bancária", "Open Finance", "Planos"]
)

# 🏠 INÍCIO
if menu == "Início":
    show_landing()

# 💳 PLANOS
elif menu == "Planos":
    plano = verificar_plano()
    st.info(f"Plano atual: {plano}")

# 🏦 CONCILIAÇÃO PDF
elif menu == "Conciliação Bancária":

    if verificar_plano() == "free":
        mostrar_upgrade()
        st.stop()

    if not pode_usar():
        mostrar_upgrade()
        st.stop()

    st.subheader("🏦 Conciliação Bancária por PDF")

    banco = st.selectbox(
        "Banco",
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
                    # 🔥 CLASSIFICAÇÃO CONTÁBIL
                    df["Categoria"] = df.apply(
                        lambda x: classificar(x["Descrição"], x["Valor"]),
                        axis=1
                    )

                    registrar_uso()

                    st.success("✅ Conciliação e classificação concluídas")
                    st.dataframe(df)

                    st.download_button(
                        "⬇️ Baixar CSV classificado",
                        df.to_csv(index=False),
                        file_name="numera_lancamentos_classificados.csv",
                        mime="text/csv"
                    )

            except Exception as e:
                st.error("❌ Erro ao processar o PDF")
                st.exception(e)

# 🌐 OPEN FINANCE (FastAPI)
elif menu == "Open Finance":
    st.subheader("🔗 Conectar Open Finance")
    st.markdown("""
        Conecte sua conta bancária através do backend seguro da NUMERA.
        Todas as movimentações serão processadas automaticamente.
    """)

    # Inserir CPF/CNPJ do cliente
    cpf_cnpj = st.text_input("CPF ou CNPJ do cliente")

    if st.button("Buscar extrato do cliente"):
        if not cpf_cnpj:
            st.warning("Informe o CPF/CNPJ")
        else:
            with st.spinner("🔄 Buscando extrato..."):
                try:
                    # Substitua pelo URL do seu backend FastAPI
                    backend_url = "https://seu-backend.herokuapp.com/extrato"

                    # Exemplo payload (você ajusta conforme backend)
                    payload = {"cpf_cnpj": cpf_cnpj}
                    resp = requests.post(backend_url, json=payload, timeout=30)

                    if resp.status_code == 200:
                        st.success("✅ Extrato recebido")
                        st.json(resp.json())
                    else:
                        st.error("❌ Erro ao buscar extrato")
                        st.text(resp.text)

                except Exception as e:
                    st.error("❌ Erro de conexão com o backend")
                    st.exception(e)

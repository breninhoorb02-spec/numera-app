import streamlit as st

def show_dashboard():
    st.title("📊 NUMERA • Dashboard")

    st.success("Plano ativo confirmado ✅")

    st.markdown("### 📁 Conciliação Bancária")

    st.file_uploader(
        "Envie o extrato bancário em PDF",
        type=["pdf"]
    )

    st.markdown("---")

    st.info("Em breve: classificação automática por IA")

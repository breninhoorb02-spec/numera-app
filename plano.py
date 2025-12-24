
import streamlit as st

def verificar_plano():
    if "plano" not in st.session_state:
        st.session_state.plano = "free"

    return st.session_state.plano

def mostrar_upgrade():
    st.warning("🔒 Recurso disponível apenas para planos pagos")
    st.markdown("👉 Faça upgrade na landing page")

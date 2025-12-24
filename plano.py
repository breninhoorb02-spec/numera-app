import streamlit as st

LIMITES = {
    "free": 1  # usuário free pode subir apenas 1 PDF
}

def verificar_plano():
    if "plano" not in st.session_state:
        st.session_state.plano = "free"

    if "usos" not in st.session_state:
        st.session_state.usos = 0

    return st.session_state.plano

def pode_usar():
    plano = verificar_plano()
    return st.session_state.usos < LIMITES[plano]

def registrar_uso():
    st.session_state.usos += 1

def mostrar_upgrade():
    st.info("🚀 Você está usando a versão FREE de teste. Faça upgrade para liberar mais PDFs.")

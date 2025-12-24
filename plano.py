import streamlit as st

LIMITES = {
    "free": 1,
    "starter": 10,
    "pro": 50
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
    st.warning("🚫 Limite do plano atingido")
    st.markdown("👉 Faça upgrade para continuar")

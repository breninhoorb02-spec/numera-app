import streamlit as st
from landing import show_landing
from dashboard import show_dashboard

st.set_page_config(page_title="Numera", layout="centered")

if "plano_ativo" not in st.session_state:
    st.session_state["plano_ativo"] = False

st.sidebar.title("NUMERA")

if st.sidebar.button("Simular plano ativo"):
    st.session_state["plano_ativo"] = True
    st.experimental_rerun()

if not st.session_state["plano_ativo"]:
    show_landing()
else:
    show_dashboard()

import streamlit as st

def verificar_limite():
    if "uploads" not in st.session_state:
        st.session_state.uploads = 0

    st.session_state.uploads += 1

    if st.session_state.uploads > 1:
        st.warning("Plano gratuito permite apenas 1 PDF.")
        st.stop()

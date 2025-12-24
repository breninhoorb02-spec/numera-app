import streamlit as st

def login():
    if "logado" not in st.session_state:
        st.session_state.logado = False

    if not st.session_state.logado:
        st.title("🔐 Login Numera")

        email = st.text_input("Email")
        senha = st.text_input("Senha", type="password")

        if st.button("Entrar"):
            if email and senha:
                st.session_state.logado = True
                st.session_state.email = email
                st.rerun()
        st.stop()

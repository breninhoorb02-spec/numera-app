import streamlit as st

def show_landing():
    st.title("🚀 NUMERA")
    st.subheader("Conciliação bancária automática com IA")

    st.markdown("""
    Transforme **PDFs bancários** em lançamentos contábeis automáticos.
    Economize horas e escale seu escritório.
    """)

    st.markdown("### 💰 Planos")
    st.markdown("""
    • Starter – R$ 49/mês  
    • Profissional – R$ 99/mês  
    • Escritórios – R$ 199/mês
    """)

    st.markdown("""
    <a href="SEU_LINK_DE_PAGAMENTO_AQUI" target="_blank">
    <button style="padding:15px;font-size:18px;">Assinar agora</button>
    </a>
    """, unsafe_allow_html=True)

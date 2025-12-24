login()
from auth import login
from plano import verificar_limite
from parser_generico import extrair_generico
from parser_nubank import extrair_nubank
import pdfplumber
import streamlit as st

def show_landing():
    st.markdown("## 🚀 NUMERA")
    st.markdown("### Conciliação bancária automática com IA")

    st.markdown("""
    A **Numera** transforma extratos bancários (PDF)  
    em **lançamentos contábeis automáticos**, em minutos.
    """)

    st.markdown("---")

    st.markdown("### ❌ O problema")
    st.markdown("""
    Conciliação manual consome horas, gera erros  
    e impede o crescimento do escritório.
    """)
pdf_file = st.file_uploader("Envie o extrato bancário (PDF)", type=["pdf"])

if pdf_file:
    verificar_limite()

    with pdfplumber.open(pdf_file) as pdf:
        texto = ""
        for page in pdf.pages:
            texto += page.extract_text() or ""

    if "nubank" in texto.lower():
        df = extrair_nubank(texto)
    else:
        df = extrair_generico(texto)

    st.dataframe(df)
    st.markdown("### ✅ A solução")
    st.markdown("""
    ✔️ Upload de extrato PDF  
    ✔️ Classificação automática por IA  
    ✔️ Relatórios prontos  
    ✔️ Economia de tempo real  
    """)

    st.markdown("---")

    st.markdown("### 💰 Planos")
    st.markdown("""
    **Starter – R$ 49/mês**  
    **Profissional – R$ 99/mês**  
    **Escritórios – R$ 199/mês**
    """)

    st.markdown("---")

    st.success("🎁 Teste grátis por 7 dias")

    st.markdown("""
    <a href="https://www.mercadopago.com.br/subscriptions/checkout?preapproval_plan_id=9fe152004c534b43ae63965e3a37feaf"
    target="_blank">
    <button style="
        padding:15px;
        font-size:18px;
        background-color:#2563eb;
        color:white;
        border:none;
        border-radius:6px;">
        👉 Assinar agora
    </button>
    </a>
    """, unsafe_allow_html=True)
if __name__ == "__main__":
    show_landing()

import streamlit as st


import instru_bliblioteca as bl

import calculadora as calc

bl.css()


if "pagina" not in st.session_state:
    st.session_state.pagina = "menu"

with st.sidebar:
    st.title("Menu: ")
    st.markdown("### Escolha para onde deseja ir : ")
    if st.button("Ir para a Calculadora Estatística", icon=":material/calculate:"):
        st.session_state.pagina = "calculadora"
    if st.button("Sla outro"):
        st.session_state.pagina = "menu"

if st.session_state.pagina == "calculadora":
    calc.calculadora()
else:
    st.write("Bem-vindo! Use o menu à esquerda para navegar.")
    

import streamlit as st
import re
import time
from sqlalchemy import create_engine
import pandas as pd
import os

            

def conCursor():
    "Faz com quese conecte ao baco de dados"
                    #Connection e Cursor
    DATABASE_URL = os.environ["DATABASE_URL"]
    engine = create_engine(DATABASE_URL)

    
    return engine

        
def css():
    "Este e o CSS do site ele deixa o tema adptavel, o botao de login no meio e o botoa de entrar"
            #Deixa o tema adaptavel
    
    is_dark = st.get_option("theme.base") == "dark"
    box_color = "#262730" if is_dark else "#FFFFFF"
    text_color = "#FFFFFF" if is_dark else "#000000"


            #Deixa o login no meio
    st.markdown("""
        <style>
        
        .login-title {
            text-align: center;
            font-size: 28px;
            font-weight: bold;
            margin-bottom: 20px;
        }
        </style>
    """, unsafe_allow_html=True)

        
            #Deixa o botão de entrar centralizado
    st.markdown("""
    <style>
    .stButton>button {
        background-color: #262730;
        color: white;
        border: none;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 32px;
        cursor: pointer;
        border-radius: 8px;
        width: 200px;
    }
    .stButton {
        display: flex;
        justify-content: center;
    }
    </style>
""", unsafe_allow_html=True)





            # Estrutura do cartão de login

        
def titulo():
    ""
    
    st.markdown('<div class="login-title">Login : </div>', unsafe_allow_html=True)


def validar_email(email):
    "Valida o e-mail do usuario com a tal definição = 'um_texto_antes_o_arroba@um_endereço_depois.com'"
    padrao = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(padrao, email) is not None

def verificar_no_db(email, senha):
    engine = conCursor()
    
    try:
        query = "SELECT * FROM usuarios WHERE email = %s AND senha = %s"
        df = pd.read_sql(query, con=engine, params=(email, senha))
    except Exception as e:
        st.error(f"Erro ao consultar o banco de dados: {e}")
        return

    if not df.empty:
        with st.empty():
            with st.spinner("Login Bem-Sucedido! Redirecionando..."):
                time.sleep(3)
                st.page_link("main.py")
    else:
        st.error("Usuário não cadastrado.")


def login1():


    email= st.text_input("E-Mail : ")
    senha = st.text_input("Senha : ", type="password")
    if st.button("Entrar"):
        if not email or not senha:
            st.error("Erro : E-mail ou senha nao insiridos.")
        elif not validar_email(email):
            st.error("Erro : O e-mail digitado não é valido !")
        else:
            verificar_no_db(email, senha)
            
    return email



st.markdown('</div>', unsafe_allow_html=True)



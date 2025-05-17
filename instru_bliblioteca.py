import streamlit as st
import re
import time
from sqlalchemy import create_engine
import pandas as pd
import os
from streamlit_extras.switch_page_button import switch_page  # <- IMPORTAÇÃO CERTA


def conCursor():
    "Faz conexão com o banco de dados"
    DATABASE_URL = os.environ["DATABASE_URL"]
    engine = create_engine(DATABASE_URL)
    return engine


def css():
    "CSS do login"
    is_dark = st.get_option("theme.base") == "dark"
    st.markdown("""
        <style>
        .login-title {
            text-align: center;
            font-size: 28px;
            font-weight: bold;
            margin-bottom: 20px;
        }
        .stButton>button {
            background-color: #262730;
            color: white;
            border: none;
            padding: 15px 32px;
            text-align: center;
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


def titulo():
    st.markdown('<div class="login-title">Login :</div>', unsafe_allow_html=True)


def validar_email(email):
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
        with st.spinner("Login Bem-Sucedido! Redirecionando..."):
            time.sleep(3)
            st.switch_page('main.py')
    else:
        st.error("Usuário não cadastrado.")


def login1():
    email = st.text_input("E-Mail : ")
    senha = st.text_input("Senha : ", type="password")
    if st.button("Entrar"):
        if not email or not senha:
            st.error("Erro : E-mail ou senha não inseridos.")
        elif not validar_email(email):
            st.error("Erro : O e-mail digitado não é válido!")
        else:
            verificar_no_db(email, senha)
    return email

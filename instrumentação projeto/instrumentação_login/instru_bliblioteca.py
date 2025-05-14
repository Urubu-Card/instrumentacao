import streamlit as st
import mysql.connector as my
import re
import time

                      


#Connection e Cursor
con = my.connect(
        host="localhost",           # Ou o IP do servidor MySQL
        user="root",                # Substitua pelo seu usuário
        password="edu123",          # Substitua pela (edu123)
        database="login"           # Nome da sua base de dados
    )

cu = con.cursor()


        
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
    padrao = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(padrao, email) is not None


def verificar_no_db(email,senha):
    colocar_no_DB ="SELECT * FROM dados WHERE email = %s AND senha = %s"
    dados = (email,senha)
    cu.execute(colocar_no_DB,dados)
    resultado = cu.fetchone()

    if resultado:
        with st.empty():
            with st.spinner("Login Bem-Sucedido! Redirecionando..."):
                time.sleep(3)
        st.switch_page("pages/main.py")
    else:
        st.error("Usuario não cadastrado. ")

    con.commit()


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
            con.close()
    return email



st.markdown('</div>', unsafe_allow_html=True)

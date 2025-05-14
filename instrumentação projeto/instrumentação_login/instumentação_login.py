import streamlit as st


st.set_page_config(page_icon="⚙",page_title="Login : ", layout="centered") 
            #Pra nao dar o erro quando entra



import instru_bliblioteca as bl
import mysql.connector as my






#Connection e Cursor
con = my.connect(
        host="localhost",           # LocalHost ou ip do Servidor
        user="root",                #Usuario
        password="edu123",          # Senha : ("edu123")
        database="login"            # Nome do banco de dados
    )

cu = con.cursor()


#Css da Pagina
bl.css()

#Titulo da PAgina
bl.titulo()


#Login
email = bl.login1()

#Valida o Email
bl.validar_email(email)


st.markdown('</div>', unsafe_allow_html=True)

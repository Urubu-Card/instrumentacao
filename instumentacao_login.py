import streamlit as st


st.set_page_config(page_icon="⚙",page_title="Login : ", layout="centered") 
            #Pra nao dar o erro quando entra


import instru_bliblioteca as bl



#Css da Pagina
bl.css()

#Titulo da PAgina
bl.titulo()


#Login
email = bl.login1()

#Valida o Email
bl.validar_email(email)



img_url = "https://raw.githubusercontent.com/Urubu-Card/instrumentacao/main/instrumentacao/instrumentacao_projeto/imagens/decorativa.png"

st.markdown(f"""
    <style>
        .bg-img {{
            position: fixed;
            bottom: 10px;
            right: 10px;
            width: 150px;
            opacity: 0.8;
            z-index: -1;
        }}
    </style>
    <img class="bg-img" src="{img_url}"/>
""", unsafe_allow_html=True)



st.markdown('</div>', unsafe_allow_html=True)


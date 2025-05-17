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


st.markdown(
    f"""
    <style>
        .logo-img {{
            position: fixed;
            top: 0px;
            left: 0px;
            width: 400px; /* ajuste conforme necessário */
            margin: 0;
            padding: 0;
            z-index: 0;
            opacity: 0.3;  /* ajuste a transparência se quiser mais suave */
        }}
    </style>
    <img class="logo-img" src="https://raw.githubusercontent.com/Urubu-Card/instrumentacao/main/instrumentacao/instrumentacao_projeto/imagens/decorativa.png"/>
    """,
    unsafe_allow_html=True
)



st.markdown('</div>', unsafe_allow_html=True)


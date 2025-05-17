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



img_url = "https://media.discordapp.net/attachments/1310238818603106345/1373329491794989207/image_1.png?ex=682a0442&is=6828b2c2&hm=6bae7e56c55bd6a68910d441f6e27e8d0b495cde07d9f9a9c0e4d2aed1cf1a0f&=&format=webp&quality=lossless"

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


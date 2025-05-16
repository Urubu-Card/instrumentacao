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


st.markdown('</div>', unsafe_allow_html=True)

import os


def listar_paginas():
    st.title("🔍 Diagnóstico de Navegação com switch_page")

    main_path = os.getcwd()
    st.write(f"📁 Diretório atual: `{main_path}`")

    # Verifica se existe a pasta 'pages'
    pages_path = os.path.join(main_path, "pages")
    if not os.path.exists(pages_path):
        st.error("❌ Pasta 'pages/' não encontrada. Crie uma pasta chamada 'pages'.")
        return

    arquivos = os.listdir(pages_path)
    arquivos_py = [f for f in arquivos if f.endswith(".py")]

    if not arquivos_py:
        st.warning("⚠️ Nenhum arquivo .py encontrado em 'pages/'.")
        return

    st.success("✅ Arquivos encontrados em 'pages/':")
    for arquivo in arquivos_py:
        nome_pagina = arquivo.replace(".py", "")
        st.write(f"- `pages/{nome_pagina}` (Use com: `st.switch_page('pages/{nome_pagina}')`)")

    st.info("👀 Use o nome da página exatamente como listado acima, sem '.py'.")

listar_paginas()

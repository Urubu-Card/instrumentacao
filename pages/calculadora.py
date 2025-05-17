def calculadora():
    import streamlit as st
    import numpy as np
    import matplotlib.pyplot as plt
    import scipy.stats as stats
    import pandas as pd


    # ------------------- INICIALIZAÇÃO DA SESSÃO -------------------

    if "mostrar_resultado" not in st.session_state:
        st.session_state.mostrar_resultado = False

    # ------------------- CONFIGURAÇÃO DA PÁGINA -------------------

    st.title("...Calculadora Estatística...")
    st.write("Insira dados para calcular média, variância, desvio padrão, incertezas e visualizar gráficos.")

    # ------------------- INTERFACE INICIAL -------------------

    st.subheader("1. Escolha se as informações que ira querer serão resultados como População ou como Amostra :")
    esco = st.selectbox("Selecione entre População ou Amostra : ",("População","Amostra"))


    st.subheader("2. Escolha a quantidade de valores e insira os dados")
    qtd = st.selectbox("Selecione a quantidade de valores (2 a 50):", options=list(range(2, 51)), key="qtd")

    valores = []
    cols = st.columns(9)  

    for i in range(qtd):
        
        col = cols[i % 9]
        with col:
            num = st.number_input(f"{i+1}° Valor", key=f"valor_{i}", step=0.01)
            valores.append(num)

    if st.button("Confirmar e calcular"):
        st.session_state.mostrar_resultado = True
        st.session_state.valores = valores

    # ------------------- RESULTADOS -------------------

    if st.session_state.mostrar_resultado:

        dados = np.array(st.session_state.valores)
        n = len(dados)
        media = np.mean(dados)

        # População
        var_pop = np.var(dados)
        desvio_pop = np.std(dados)

        # Amostra
        var_amostral = np.var(dados, ddof=1)
        desvio_amostral = np.std(dados, ddof=1)

        # Incerteza padrão
        u_padrao = desvio_amostral / np.sqrt(n)

        # Incerteza expandida (k=2)
        k = 2
        u_expandida = k * u_padrao

        # Intervalo de confiança (95%) com t de Student
        gl = n - 1
        t_student = stats.t.ppf(0.975, df=gl)  # 95% bilateral
        margem_erro = t_student * u_padrao
        intervalo = (media - margem_erro, media + margem_erro)
            
        

        
        st.divider()
        st.subheader("Resultados Estatísticos : ")

        st.markdown(f"### **Média :** {media:.4f}")
        st.divider()
        col1, col2 = st.columns(2)

        if esco =="População":
            st.markdown("### Cálculos como População:")
            st.markdown(f"### Variância:  {var_pop:.4f}")
            st.markdown(f"### Desvio padrão: {desvio_pop:.4f}")
        elif esco=="Amostra":
            st.markdown("### Cálculos como Amostra:")
            st.markdown(f"### Variância: {var_amostral:.4f}")
            st.markdown(f"### Desvio padrão: {desvio_amostral:.4f}")
            st.markdown(f"### Incerteza padrão (u): {u_padrao:.4f}")
            st.markdown(f"### Incerteza expandida (U, k=2): {u_expandida:.4f}")
            st.markdown(f"### Intervalo de confiança 95%: [{intervalo[0]:.4f}, {intervalo[1]:.4f}]")
        
        # ------------------- GRÁFICO -------------------
        
        
                        #Deixa o Grafico tansparente 
        fig, ax = plt.subplots(facecolor = "none")
        fig.patch.set_alpha(0)
        ax.set_facecolor('none')


                        #Deixa a cor dos graficos branca pra ser mais visiveis

        ax.spines['bottom'].set_color('white')              # Linha inferior
        ax.spines['left'].set_color('white')                # Linha esquerda
        ax.xaxis.label.set_color('white')                   # Título do eixo X
        ax.yaxis.label.set_color('white')                   # Título do eixo Y
        ax.title.set_color('white')                         # Título do gráfico
        ax.tick_params(axis='x', colors='white')            # Cor dos números no eixo X
        ax.tick_params(axis='y', colors='white')            # Cor dos números no eixo Y
        ax.title.set_fontweight('bold')                    


        
        ax.hist(dados, bins='auto', color='#262730', edgecolor='black')
        ax.axvline(media, color='red', linestyle=':', label='Média')
        ax.set_title("Distribuição dos Valores",fontweight='bold')
        ax.set_xlabel("Valor",fontweight='bold')
        ax.set_ylabel("Frequência",fontweight='bold')
        ax.legend()
        st.pyplot(fig)
        
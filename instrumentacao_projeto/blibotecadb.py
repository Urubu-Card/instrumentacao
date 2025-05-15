import sqlite3 as sq
import streamlit as st
import mysql.connector as my
import re

con = my.connect(
        host="localhost",           # Ou o IP do servidor MySQL
        user="root",                # Substitua pelo seu usuário
        password="edu123",          # Substitua pela (edu123)
        database="login"           # Nome da sua base de dados
    )

cur = con.cursor()

    
def validar_email(email):
    padrao = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(padrao, email) is not None


def criar_banco():

    cur.execute(
        '''
        CREATE TABLE IF NOT EXISTS Tarefas(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        descricao TEXT,
        status TEXT
        )

    ''')

def primeiro():
    
    print("Qual ação deseja fazer?" \
    "\n 1-- Adicionar novo usuario ao banco de dados" \
    "\n 2-- Listar todos os usuarios no banco de dados" \
    "\n 3-- Deletar um usuario")

    resp = int(input())
    return resp

def peguntas():


    print("Digite o email do usuario : ")

    while True:
        email = input("")
        if not validar_email(email):
            print("Erro : O email digitado não é valido !")
        else:
            break
    print("Digite a senha do usuario : ")

    senha = input("")


    cur.execute('''
        INSERT INTO dados (email,senha)
        VALUES(%s,%s)


    ''',(email,senha)
    )
    con.commit()

    print("Deseja fazer outra ação? ")
    r = input().strip().lower().capitalize()

def listar ():
    cur.execute("""
        SELECT id, email , senha FROM dados
        ORDER BY id ASC
    """)

    pesquisa = cur.fetchall()
    if pesquisa:
        for i in pesquisa:
            print('-------')
            print(f"ID = {i[0]}")
            print('-------')
            print(f"E-mais  = {i[1]}")
            print('-------')
            print(f"Senhas = {i[2]}")
            print('-------')
    else:
        print("---Nenhum usuario registrado---")
    print("Deseja fazer outra ação? ")
    r = input()


def deletar():
    print("Qual id deseja deletar? ")
    deleteid= int(input())

    cur.execute(""" 
        DELETE FROM dados WHERE id = %s

    """,(deleteid,))
    con.commit()
    
    print("---Tarefa Deletada com sucesso---")
    print("Deseja fazer outra ação? ")
    r = input().strip().lower().capitalize()

def closecon():
    cur.close()
    con.close()


def erro():
    print("---A ação que você selecionou esta erada--- ")
    r="Sim"


def stpesq():

    desc = st.text_input("Descreva a tarefa", key="desc_input")

    sta = st.text_input("Qual o Status da tarefa? (Pendente ou Concluída)", key="status_input")
    valid_status = sta.strip().lower().capitalize() in ["Pendente", "Concluida"]

    if sta and not valid_status:
        st.error("Forma de Status errada. Tente novamente (Pendente ou Concluída).")

    if st.button("Adicionar Tarefa") and desc and valid_status:
        sta = sta.strip().lower().capitalize()
        cur.execute(
            '''
            INSERT INTO Tarefas (descricao, status)
            VALUES (?, ?)
        ''',
            (desc, sta)
        )
        con.commit()
        st.success("Tarefa adicionada com sucesso!")

def stlist():
    st.header("Qual e o id da tarefa que deseja deletar ? ")
    delid = st.number_input("ID da Tarefa :",min_value=1,step=1,label_visibility="collapsed")
    if st.button("Deletar Tarefa"):
        cur.execute(""" 
        DELETE FROM Tarefas WHERE id = ?

    """,(delid,))
        con.commit()
        st.success("---Tarefa Deletada com sucesso---")



def stpri():
    
    st.header("Qual ação deseja fazer?")
    add = st.button("Adicionar nova tarefa : ")
    lista = st.button("Listar todas as tarefas : ")
    dele = st.button("Deletar uma tarefa : ")
    if add:
        stpesq()
    elif dele:
        stlist()
    





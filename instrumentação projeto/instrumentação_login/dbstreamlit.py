import blibotecadb as db
import streamlit as st
import sqlite3 as sq

st.set_page_config(page_icon="❗",page_title="Tarefas : ",layout="centered",)


con = sq.connect("tarefas.db")
cur = con.cursor()



cur.execute(
    '''
    CREATE TABLE IF NOT EXISTS Tarefas(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    descricao TEXT,
    status TEXT
    )

''')





st.title("Gerenciador de Tarefas : ")

db.stpri()
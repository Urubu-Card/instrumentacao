import streamlit as st
from streamlit_extras.switch_page_button import switch_page

if st.button("Testar navegação"):
    switch_page("pages/main")

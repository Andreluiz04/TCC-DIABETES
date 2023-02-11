import streamlit as st
from web_functions import load_data
from Tabs import home, data, predict, visualise

#configurando o aplicativo
st.set_page_config(
    page_title = 'TCC Sobre Diabetes',
    page_icon = 'random',
    layout = 'wide',
    initial_sidebar_state = 'auto'
)

Dicionario de Paginas
Tabs = {
    "Iniciar": home,
    "Dados": data,
    "Predicao": predict,
    "Visualizacao": visualise
}
#para executar utilizar a seguinte função: python -m streamlit run main.py

import streamlit as st
from web_functions import load_data
from Tabs import home, data, predict, visualise

# configurando o aplicativo
st.set_page_config(
    page_title = 'TCC Sobre Diabetes',
    page_icon = 'random',
    layout = 'wide',
    initial_sidebar_state = 'auto'
)

#Dicionario de Paginas
Tabs = {
    "Iniciar": home,
    "Dados": data,
    "Predicao": predict,
    "Visualizacao": visualise

# Criando um subtitulo
# Adicionando subtitulo na barra lateral
st.sidebar.title("Navegaçao")

#criando a opção de radio para selecionar a pagina
page = st.sidebar.radio("Paginas", list(Tabs.keys()))

#carregando os dados
df, X, y = load_data()

#chamando a função para executar a pagina
if page in ["Predicao", "Visualizacao"]:
    Tabs[page].app(df, X, y)
elif (page == "Dados"):
    Tabs[page].app(df)
else:
    Tabs[page].app()

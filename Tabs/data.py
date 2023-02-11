"""Este modulo tem dados sobre a pagina inicial"""

#importando modulos necessarios
import streamlit as st

def app(df):
    """criando a pagina de informações dos dados"""
    st.title("pagina dos dados")

    #adicionando subtitulo para a função
    st.subheader("Ver Dados")

    #criando expansão para ver os dados
    with st.expander("Ver Dados"):
      st.dataframe(df)
        
    #criando seção para os valores das colunas
    st.subheader("Descrição das colunas:")

    #criando checkbox para obter o resumo
    if st.checkbox("Exibir Resumo"):
        st.dataframe(df.describe())3

    #criando caixas de seleção em linhas
    col_name, col_dtype, col_data = st.columns(3)

    #mostrando nomes dos dataframes
     with col_name:
        if st.checkbox("Nome das colunas"):
            st.dataframe(df.columns)

    #mostrando o tipo de dados das colunas
    with col_dtype:
        if st.checkbox("Tipos de Dados das Colunas"):
            dtypes = df.dtypes.apply(lambda x: x.name)
            st.dataframe(dtypes)

    #mostrando od dados de cada coluna
    with col_data: 
        if st.checkbox("Dados das Colunas"):
            col = st.selectbox("Nome das Colunas", list(df.columns))
            st.dataframe(df[col])
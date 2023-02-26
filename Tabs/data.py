# Importando modulos necessarios
import streamlit as st


def app(df):
    """crianção da pagina de dados"""

    # Adicinando titulo para a pagina
    st.title("Pagina de Dados")

    st.subheader("Visualizar dados")

    with st.expander("Visualizar dados"):
        st.dataframe(df)

    st.subheader("Coluna de Descrição:")

    if st.checkbox("Sumario"):
        st.dataframe(df.describe())

    col_name, col_dtype, col_data = st.columns(3)

    with col_name:
        if st.checkbox("Nome das Colunas"):
            st.dataframe(df.columns)

    with col_dtype:
        if st.checkbox("Tipo de Dados da Coluna"):
            dtypes = df.dtypes.apply(lambda x: x.name)
            st.dataframe(dtypes)
    
    with col_data: 
        if st.checkbox("Dados da Coluna"):
            col = st.selectbox("Nome da Coluna", list(df.columns))
            st.dataframe(df[col])

    st.markdown("""
                    <p style="font-size:24px">
                        <a 
                           >Get Datasete
                        </a> 
                    </p>
                """, unsafe_allow_html=True
    )
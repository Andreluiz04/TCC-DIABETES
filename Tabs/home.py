import streamlit as st

def app():
    """Função para criar a pagina Inicial"""
    
    # Adicionando um titulo
    st.title("TCC sobre Diabetes")

    # Adicionando uma imagem
    st.image("./images/home.png")

    st.markdown("""
                    <p style="font-size:24px">
                        <a 
                           >Get Datasete
                        </a> 
                    </p>
                """, unsafe_allow_html=True
    )

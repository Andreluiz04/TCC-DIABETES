"""Este modulo tem dados sobre a pagina inicial"""

#importando modulos necessarios
import streamlit as st

def app():
	#adicionando titulo do trabalho
	st.title("TCC sobre Diabetes")

	#adicionar uma imagem na pagina inicial
	st.image("./Imagens/inicial.JFIF")

	#Breve descrição do aplicativo sobre diabetes
	 st.markdown(
    """<p style="font-size:20px;">
    
    </p>
    """, unsafe_allow_html=True)
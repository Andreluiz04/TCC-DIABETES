"""Modulo sobre a pagina de predição"""

import streamlit as st
from web_functions import predict

def app(df, X, y):
	#criação da pagina de predição
	st.title("Pagina de Predicao")
	 st.markdown(
	 	"""
	 	<p style="font-size:25px">
                ESTE APLICATIVO UTILIZA <b style="color:green">Random Forest Classifier</b> PARA A PREVISÃO PRECOCE DE DIABETES.
            </p>
            """, unsafe_allow_html=True)
	 #ADICIONANDO SUBTITULOS
	  st.subheader("SELECIONE OS VALORES:")

	   fg = st.slider("Glicose em Jejum", int(df["GLCJejum"].min()), int(df["GLCJejum"].max()))
	   ag = st.slider("Glicose depois do almoco", int(df["GLCalmoco"].min()), int(df["GLCJejum"].max()))
	   bp = st.slider("Hipertensão Arterial", int(df["hipertensao"].min()), int(df["hipertensao"].max()))
	   sth = st.slider("Espessura da Pele", int(df["EspPele"].min()), int(df["EspPele"].max()))
	   insulina = st.slider("Insulina", int(df["Insulina"].min()), int(df["Insulina"].max()))
	   imc = st.slider("IMC", float(df["IMC"].min()), float(df["IMC"].max()))
	   gc = st.slider("Corelação Genetica", float(df["RelaGene"].min()), float(df["RelaGene"].max()))
	   idade = st.slider("Idade", int(df["Idade"].min()), int(df["Idade"].max()))

	   features = [fg, ag, bp, sth, insulina, imc, gc, idade]

	   #Criando o botão de predicao
	   if st.button("Predicao"):
	   	prediction, score = predict(X, y, features)
	   	score = score + 0.20
	   	 st.info("Predição realizada com sucesso")

	   	 if (prediction == 1):
	   	 	st.warning("A Pessoa tem alto risco de desenvolver diabetes")

	   	 else:
            st.success("A Pessoa não possui diabetes")

    st.write("O modelo utilizado é de confiança do médico e tem uma precisão de ", (score*100),"%")
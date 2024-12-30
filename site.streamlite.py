import streamlit as st
import pandas as pd

st.set_page_config(page_title="meu site streamlit")

with st.container():
 st.subheader("meu primeiro site com streamlit")
 st.title("Dashboard de Contratos")
 st.write("Informações dos contratos fechados pela empresa de fulano ao longo de maio")
 st.write("Quer aprender como esse site foi feito? [Clique aqui](https://www.fluminense.com.br/site/) ")

@st.cache_data 
def carregar_dados():
 tabela = pd.read_csv("resultados.csv")
 return tabela


with st.container():
 st.write("---")
 qtde_dias = st.selectbox("Selecione o período", ["7d", "15d", "21d", "30d"])
 num_dias = int(qtde_dias.replace("d", ""))
 dados = carregar_dados()
 dados = dados[-num_dias:]
 st.area_chart(dados, x="Data", y="Contratos") 
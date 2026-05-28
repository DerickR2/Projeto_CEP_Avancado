import streamlit as st
from ferramentas import buscar_cep
import pandas as pd

st.sidebar.title("CEP Skyline")
st.sidebar.image("CEP-SKYLINE.png")
cep = st.sidebar.text_input("Digite o CEP que deseja consultar: ")

if st.sidebar.button("Consultar"):
    dados = buscar_cep(cep)
    lat = float(dados.get("lat"))
    lng = float(dados.get("lng"))

    cordenadas = pd.DataFrame({"latitude":[lat],  "longitude":[lng]})
    st.map(cordenadas, zoom=15, color="#00e1e9d6")
    
    st.json(dados)
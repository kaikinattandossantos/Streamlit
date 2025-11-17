import streamlit as st
import pandas as pd

st.header("Leitura de Arquivo CSV")

arquivo = st.file_uploader("Envie um arquivo .csv")

if arquivo:
    df = pd.read_csv(arquivo)
    st.dataframe(df)

import streamlit as st

st.header("Cálculo de IMC")

peso = st.number_input("Peso (kg)", min_value=0.0)
altura = st.number_input("Altura (m)", min_value=0.0)

if st.button("Calcular IMC"):
    if peso > 0 and altura > 0:
        imc = peso / (altura ** 2)
        st.write(f"**IMC:** {imc:.2f}")

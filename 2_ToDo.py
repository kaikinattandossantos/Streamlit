import streamlit as st

st.header("Lista de Tarefas")

if "tarefas" not in st.session_state:
    st.session_state.tarefas = []

tarefa = st.text_input("Digite uma tarefa")

if st.button("Adicionar"):
    st.session_state.tarefas.append(tarefa)

st.subheader("Tarefas:")

for t in st.session_state.tarefas:
    st.write(f"- {t}")

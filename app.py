import streamlit as st
from crud import criar_aluno, listar_alunos, atualizar_idade, deletar_aluno

st.set_page_config(page_title="Gerenciamento de alunos", page_icon="🐷")

st.title("Sistema de alunos com PostgreSQL")

menu = st.sidebar.radio("Menu", ["Inserir", "Listar", "Atualizar", "Deletar"])

if menu == "Inserir":
    st.subheader("➕Inserir alunos")
    nome = st.text_input("Nome", placeholder="Seu nome")
    idade = st.number_input("Idade", min_value=16, step=1)
    if st.button("Cadastrar"):
        if nome.strip() != "":
            criar_aluno(nome, idade)
            st.success(f"Aluno {nome} inserindo com sucesso!")
        else:
            st.warning("O campo não pode estar vazio.")
elif menu == "Listar":
    st.subheader("Listar Alunos")
    alunos = listar_alunos()
    if alunos:
        for linha in alunos:
            st.write(f"ID= {linha[0]} | NOME= {linha[1]} | IDADE= {linha[2]}")
        else:
            st.info("Nenhum aluno encontrado. ")



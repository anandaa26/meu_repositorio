import streamlit as st
import pandas as pd


st.title('Motos')
st.image('s1000.png')
st.image('160 titan.png')

st.sidebar.image('logo.png')
opcoes = ['s1000','160 titan']


selecionado = st.sidebar.selectbox('Escolha uma opção:', opcoes)

st.write(f'Você selecionou: {selecionado}')
st.link_button(url = 'https://www.honda.com.br/motos/street/city/cg-160-titan',label= "comprar")

if opcoes == 's1000':
    st.image('s1000.png')
elif opcoes == '160 titan':
    st.image('160 titan.png')

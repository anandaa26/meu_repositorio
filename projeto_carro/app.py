import streamlit as st
st.sidebar.title("aluguel de carros")
st.sidebar.image("logo.png") 
st.sidebar.write("esclha o carro ideal para voce")
carro = ["gol", "BMW", "corsa", "toro"]
st.sidebar.selectbox("selecione o modelo do carro:", carro)

st.sidebar.image("ligo.png")
st.sidebar.title('Ananda carros')



carros = ['BMW','mustang', 'porsche', 'toro']

opçao = st.sidebar.selectbox('escolha o carro que foi alugado', carros)




st.title('kamilly carros - aluguel de carros')

st.image(f'{opçao}.png')
st.markdown(f'## voce alugou o modelo :{opçao}')
st.markdown('---')

dias = st.text_input(f'por quantos dias o {opçao} foi alugado?')
km = st.text_input(f'quntos km vc rodou com o {opçao}?')


if opçao == 'BMW':
    diaria = 450
elif opçao == 'mustang':
    diaria =500
elif opçao == 'porsche':
    diaria = 300
elif opçao == 'fusca':
    diaria = 250
elif opçao == 'toro':
    diaria = 550


if st.button('calcular'):
    dias= int(dias)
    km = float(km)

    total_dias = dias * diaria
    total_km = km * 0.15
    aluguel_total = total_dias + total_km

    st,Warning(f'voce alugou o {opçao} por {dias} dias e rodou {km}. o valor total a pagar e R${aluguel_total:.2f}')
    
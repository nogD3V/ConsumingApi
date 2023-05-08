import json
import requests
import pandas as pd
import streamlit as st

#---------------INTERFACE----------------------------------
#Configurando o titulo da aba + icon da pagina + deixando o layout centralizado e deixando a sidebar em automatico.
st.set_page_config(page_title='API', page_icon=':wave:', layout="wide", initial_sidebar_state="auto")

#Definindo o titulo da página.
st.title('DEPUTADOS')

#Usando style.css para manipular o estilo da página do streamlit.
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

#---------------/FIM INTERFACE----------------------------------

#---------------API---------------------------------------------

#Definindo a variavel onde o link será armazenado.
url = "https://dadosabertos.camara.leg.br/api/v2/deputados?ordem=ASC&ordenarPor=nome"

#Fazendo a requisição com o modo get do requests.
json_url = requests.get(url)

#Carregando os dados dentro de um arquivo.txt com json.
data = json.loads(json_url.text)
#---------------/FIM API---------------------------------------------

#---------------DATA FRAME-------------------------------------------
#Criando um data frame com pandas.
#Como a API puxa as informações de DADOS e LINKS, vamos deixar claro com [] que iremos puxar somente as info de DADOS.
df = pd.DataFrame(data['dados'])
#---------------/FIM DATA FRAME-------------------------------------------

#Adicionando Dataframe na interface
st.dataframe(df)
import pandas as pd
import streamlit as st
import re

#st.title('NETFLIX SIMULATOR')
#st.subheader('Bryan Valerio Reyes')
#st.write('ZS20006768')
st.markdown("<h1 style='text-align: center; color: red;'>NETFLIX SIMULATOR</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: black;'>Bryan Valerio Reyes</h3>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: black;'>zs20006768</h3>", unsafe_allow_html=True)

DATA_URL = 'https://raw.githubusercontent.com/BryanVRe/streamlit/master/movies.csv'

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows, encoding_errors='ignore')
    return data

@st.cache
def load_data_name(name):
    datafiltered = load_data(500)
    filtrar_data_nombre = datafiltered[datafiltered['name'].str.contains(name, flags=re.IGNORECASE)]  
    return filtrar_data_nombre

@st.cache
def load_data_director(director):
    data = load_data(500)
    filtrar_data_director = data[data['director'] == director]
    return filtrar_data_director


st.sidebar.image('https://raw.githubusercontent.com/BryanVRe/streamlit/master/BRYAN.jpg')

sidebar = st.sidebar
agree = sidebar.checkbox("Mostrar todos los filmes")
titulo = sidebar.text_input('Titulo del filme:')
btnFiltrarDirectorFilm = sidebar.button('Buscar filmes')
data = load_data(500)
selected = sidebar.selectbox("Seleccionar director", data['director'].unique())
btnFiltrarDirector = sidebar.button('Filtrar por Director')

if agree:
    estado = st.text('Cargando...')
    data = load_data(500)
    estado.text("¡Cargado! (usando st.cache)")
    st.dataframe(data)

if btnFiltrarDirectorFilm:
    st.write ("Titulo buscado: "+ titulo)
    filtrar = load_data_name(titulo)
    filas = filtrar.shape[0]
    st.write(f'Total de filmes mostrados: {filas}')
    st.dataframe(filtrar)

if btnFiltrarDirector: 
    st.write("filmes dirigidas por "+selected)
    filtrar = load_data_director(selected)
    filas = filtrar.shape[0]
    st.write(f'Total de filmes: {filas}')
    st.dataframe(filtrar)
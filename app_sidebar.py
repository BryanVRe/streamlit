import streamlit as st

st.title("App con sidebar")
# Creamos el sidebar
sidebar = st.sidebar
# Agregamos un titulo y texto al sidebar
sidebar.title("Esta es el sidebar")
sidebar.write("Datos del sidebar")

st.header("Header 1")
st.header("Header 2")
st.write("Datos del content")


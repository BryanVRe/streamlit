import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

titanic_link = '/content/titanic.csv'

titanic_data = pd.read_csv(titanic_link)

fig, ax = plt.subplots()

ax.hist(titanic_data['class'])

st.header("Histograma del Titanic")

st.pyplot(fig)

st.markdown("___")

st.dataframe(titanic_data)
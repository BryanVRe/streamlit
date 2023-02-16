import streamlit as st
import pandas as pd

st.title('Streamlit - Search ranges')

data_url = ('https://firebasestorage.googleapis.com/v0/b/streamlit-bryan.appspot.com/o/csv%2Fdataset.csv?alt=media&token=48c75cb5-4cfd-4a8d-bb5b-fc48b5901a6f')

def load_data():
    data = pd.read_csv(data_url)
    return data

def load__data_bysex(sex):
    data = pd.read_csv(data_url)
    filtered__data_bysex = data[data[ 'sex'] == sex]
    return filtered__data_bysex

data = load_data()

selected_sex = st.selectbox( " Select Sex", data['sex' ].unique())
btnfilterbysex = st.button("Filter by sex")

if (btnfilterbysex):
    filterbysex = load__data_bysex(selected_sex)
    count_row = filterbysex.shape[0] # Gives number of rows
    st.write(f"Total items: {count_row}")
    st.dataframe(filterbysex)
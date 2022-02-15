import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

@st.cache
def load_data():
    df = pd.read_csv('losses2015_transformed.csv', index_col='State_Code')
    return df

st.title('Losses 2015')

# load the data
df = load_data()

# show the data in a table
if st.sidebar.checkbox('Show dataframe'):
    st.write(df)

if st.sidebar.checkbox('Damage Result'):
    df1 = df.groupby(['Damage_Descp']).mean('Amount')
    df1.reset_index()
    st.bar_chart(df1)

if st.sidebar.checkbox('States Amount'):
    df1 = df.groupby(['State_Abv']).sum('Amount')
    df1.reset_index()
    st.bar_chart(df1)

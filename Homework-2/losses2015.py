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
    df1 = df.groupby(['Damage_Descp']).mean('Amount').sort_values(by=['Amount'])
    st.bar_chart(df1)

if st.sidebar.checkbox('States Amount'):
    df1 = df.groupby(['State_Abv']).sum('Amount').sort_values(by=['Amount'])
    st.bar_chart(df1)

# choose the sources of interest
# cols = ['Coal_MW', 'Gas_MW', 'Hidroelectric_MW', 'Nuclear_MW', 'Wind_MW', 'Solar_MW', 'Biomass_MW']
# option = st.multiselect('What sources do you want to display?', cols, cols[0])
# option = st.multiselect('What sources do you want to display?', cols, cols[0])
# cols = ['amount']
# option = st.multiselect('What sources do you want to display?', cols, cols[0])


# if st.sidebar.checkbox('Show Streamlit line_chart'):
#     st.line_chart( df[option] )
# else:
#     fig, ax = plt.subplots()
#     df[option].plot(ax=ax)
#     st.write( fig )    

# if st.sidebar.checkbox('Show mean daily production'):
#     # assuming mean daily production is just reffering to the data point for each day?
#     st.write( df[option])
#     st.bar_chart(data=df[option], width=0, height=0, use_container_width=True)

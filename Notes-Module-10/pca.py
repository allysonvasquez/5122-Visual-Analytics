from pycaret.datasets import get_data
import altair as alt
import streamlit as st
from pycaret.classification import *

@st.cache
def return_pca_dataset():
    # get data   
    df_data = get_data('satellite')

    # model   
    clf = setup(data = df_data, target = 'Class', 
                       data_split_shuffle=False, 
                       pca=True, 
                       silent=True, verbose=False)

    # train logistic regression model
    lr = create_model('lr', verbose=False)

    # predictions & data preparation for visualization
    pred_pca = predict_model(lr, verbose=False)
    pred_pca['Error'] = pred_pca['Class'] != pred_pca['Label'].astype(str)

    return pred_pca

# get data for visualization
pred_pca = return_pca_dataset()

# altair plot
ch_pca = alt.Chart(pred_pca).mark_point().encode(
           x = 'Component_1:Q',
           y = 'Component_2:Q',
           color = 'Class:N',
           size = 'Error:N', 
           tooltip = ['Class', 'Label', 'Score']
).properties(
    width=800,
    height=600
).interactive()

# Show 
st.write(ch_pca)
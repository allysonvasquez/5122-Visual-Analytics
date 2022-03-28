import streamlit as st
import pandas as pd
from pycaret.regression import *

# load model
@st.cache 
def predict_cache(test_data):
    rf_saved = load_model('rf_model')
    predictions = predict_model(rf_saved, data = test_data)
    return predictions['Label']

# Inputs
inp_sex = st.radio('Sex', ('female', 'male'), index=0)
inp_smoker = st.radio('Smoker', ('no', 'yes'), index=0)
inp_region = st.radio('Region', ('southeast', 'southwest', 'northeast', 'northwest'), index=0)
inp_age = st.slider('Age', 18, 64, 35, step=1)
inp_bmi = st.slider('BMI', 15.0, 54.0, 21.0, step=0.1)
inp_children = st.slider('Children', 0, 5, 0, step=1)

test_data = pd.DataFrame({'age': [inp_age], 
                          'sex': [inp_sex], 
                          'bmi': [inp_bmi], 
                          'children' : [inp_children], 
                          'smoker': [inp_smoker], 
                          'region': [inp_region]})

# Show prediction
st.write('Insurance charges = $%0.2f'%predict_cache(test_data)[0])
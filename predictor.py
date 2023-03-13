import streamlit as st
import pickle 
import pandas as pd
import numpy as np
import base64

car_predict = pickle.load(open('LinearRegressionModel.pkl','rb'))
car_data = pd.read_csv('Cleaned_car.csv')

st.set_page_config(page_title="car Price Prediction App",layout="wide")

st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
.css-1j6homm e1tzin5v0{
margin: 1px;
}
</style> """, unsafe_allow_html=True)

# Change background image
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('car.jpg')   


custom_css = """
<style>
.css-18e3th9 {
  padding-top: 1px;
  padding-bottom: 0px;
  
}
</style>
"""

# Call st.markdown() with the custom CSS style
st.markdown(custom_css, unsafe_allow_html=True)

col1, col2 = st.columns([1.1, 1.1])
with col1:
    st.title('Car price predictor')

    company = st.selectbox('Company', car_data['company'].unique())
    car_model = st.selectbox('Car_model', car_data['name'].unique())
    year = st.selectbox('Year', car_data['year'].unique())
    fuel_type = st.selectbox('fuel_type', car_data['fuel_type'].unique())
    kms_driven= st.selectbox('Kilo_driven', sorted(car_data['kms_driven'].unique()))


if st.button('Predict Price'):
    prediction=car_predict.predict(pd.DataFrame(columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'],
                              data=np.array([car_model,company,year,kms_driven,fuel_type,]).reshape(1, 5)))
    if int(np.round(prediction[0],4)) <0:
        st.text("The vehicle have no market value")

    else:
        st.text("Estimated price : ₹" + str(np.round(prediction[0],4)))


   
import streamlit as st
import numpy as np
import pandas as pd
from pandas import DataFrame

st.write('This is the Widgets app file : ')

name = st.text_input("Enter your full name:")
if name:
    st.write(f"Hello {name} Welcome to my WebApp!!!!!!!!!!!!!!")
    
## Slider component
st.write('This is the slider widget : ')
age = st.slider("Select a value", 0, 100, 25)
st.write(f"your age is:{age}")

## Select box component
st.write('This is the select box : ')
option = st.selectbox("Select your language:", ["C++", "Java", "Python", "C"])
st.write(f"You selected: {option}")

## sample data(csv)
data = {
    'NAME' : ['TUSHAR', 'DHRUV', 'JATIN'],
    'AGE' : [20, 21, 22],
    'COUNTRY' : ['INDIA', 'USA', 'CANADA']
}

df = DataFrame(data)
df.to_csv('sampledata.csv')
st.write(df)


## Upload file component
st.write('This is the upload file widget : ')
uploaded_file = st.file_uploader("Choose a file",type=['txt','csv'])
if uploaded_file is not None:
    st.write("File uploaded successfully!")
    st.write("File details:", uploaded_file.name, uploaded_file.type, uploaded_file.size)
    df = pd.read_csv(uploaded_file)
    st.write(df)
    



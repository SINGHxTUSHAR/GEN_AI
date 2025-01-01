import streamlit as st
import pandas as pd
import numpy as np

## Title of the web app
st.title('This is the Web-App : Welcome BABY!!!!!')

## Write a simple text
st.write('*******************This is the webApp to test the streamlit app*********************')

## Simple dataframe
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

## Display the dataframe
st.write('This is my dataframe :')
st.write(df)

##create a line chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])
st.write('This is my line chart :')
st.line_chart(chart_data)
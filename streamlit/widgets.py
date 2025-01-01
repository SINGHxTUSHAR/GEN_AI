import streamlit as st
import numpy as np
import pandas as pd

st.write('This is the Widgets app file : ')

name = st.text_input("Enter your full name:")
if name:
    st.write(f"Hello {name} Welcome to my WebApp!!!!!!!!!!!!!!")
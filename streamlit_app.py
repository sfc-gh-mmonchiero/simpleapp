import streamlit as st
# import sys
import os

st.title("Test App 57")

value = st.slider("Pick a number", 0, 10, 3)

option = st.selectbox('Make a choice', ['A', 'B'])

st.write('test edit')

st.write(option)

st.write(os.getcwd())

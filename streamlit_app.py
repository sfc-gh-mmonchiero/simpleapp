import streamlit as st
import sys

st.title("Test App 31")

value = st.slider("Pick a number", 0, 10, 3)

st.write(value)
sys.stdout.write(str(value) + "\n")
sys.stdout.flush()

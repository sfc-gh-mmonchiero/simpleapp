import streamlit as st
import os

st.title("Test App 35")

value = st.slider("Pick a number", 0, 10, 3)
os.system("echo test >> text")

st.write(value)
sys.stdout.write(str(value) + "\n")
sys.stdout.flush()

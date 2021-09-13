import streamlit as st
import sys

st.title("Test App 25")

l = []
for i in range(0, 3*1024*1024*100):
    l.append(True * 1024/8)

value = st.slider("Pick a number", 0, 10, 3)

st.write(value)
sys.stdout.write(str(value) + "\n")
sys.stdout.flush()

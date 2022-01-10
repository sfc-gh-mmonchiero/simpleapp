import streamlit as st
# import sys
import os

st.title("Test App 48")

value = st.slider("Pick a number", 0, 10, 3)
st.write(os.getcwd())

f = open("text", "a")
f.write("something")
f.close()
#os.system("echo test >> text")

# st.write(value)
# sys.stdout.write(str(value) + "\n")
# sys.stdout.flush()

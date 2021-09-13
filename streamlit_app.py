import streamlit as st
import sys

st.title("Test App 25")

p = st.slider("memory parm", 0.0, 1.0, 1.0)

l = []
for i in range(0, int(p*3*1024*1024*100)):
    l.append(True * 1024/8)

agree = st.checkbox('Garbage collection')
if agree:
  import gc
  del l
  gc.collect()
value = st.slider("Pick a number", 0, 10, 3)

st.write(value)
sys.stdout.write(str(value) + "\n")
sys.stdout.flush()

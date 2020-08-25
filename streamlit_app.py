import streamlit as st

st.title("Test App!!!")

value = st.slider("Pick a number", 0, 10, 3)

st.write(value)

input = st.text_input("Tell me something", "Cantami o Diva")

st.write("Streamlit is fabulous")

print("this is a log line with ansi code:  \e[101mLight red")
print("Hello Matteo")
print("From the user:", input)

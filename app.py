import streamlit as st

st.title("Streamlit-додаток")
name = st.text_input("Як тебе звати?")
if name:
    st.success(f"Радий вас бачити, {name}!")

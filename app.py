import streamlit as st

st.title("Streamlit-додаток")
st.write("Для перевірки напишіть '1234'")
name = st.text_input("Write here")
if name:
    st.success(f"Радий вас бачити, {name}!")

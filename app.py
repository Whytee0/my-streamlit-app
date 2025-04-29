import streamlit as st

st.title("Streamlit-додаток")
st.write("Streamlit дозволяє швидко створювати веб-додатки на Python.")
name = st.text_input("Як тебе звати?")
if name:
    st.success(f"Радий тебе бачити, {name}!")

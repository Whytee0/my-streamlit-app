import streamlit as st

st.title("Streamlit-додаток")
st.write("Для перевірки напишіть '1234'")
name = st.text_input("Write here")
answer = "1234"
if name == answer:
    st.success(f"Перевірка успішно пройдена")
elif:
    st.success(f"Перевірка не пройдена")

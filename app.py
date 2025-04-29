import streamlit as st

st.title("Streamlit-додаток")
st.write("Для перевірки напишіть '1234'")
name = st.text_input("Введіть відповідь")
answer = "1234"

if st.button("Перевірити"):
    if name == answer:
        st.success("Перевірка успішно пройдена")
    else:
        st.error("Перевірка не пройдена")

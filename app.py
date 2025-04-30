import streamlit as st

st.markdown(
    "<h1 style='text-align: center; color: white;'>Streamlit додатокк</h1>",
    unsafe_allow_html=True
)
st.write("Для перевірки напишіть '1234'")
name = st.text_input("Введіть відповідь")
answer = "1234"

if st.button("Перевірити"):
    if name == answer:
        st.success("Перевірка успішно пройдена")
    else:
        st.error("Перевірка не пройдена")

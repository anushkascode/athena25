import streamlit as st

st.write("Hello world")
yes = st.checkbox("Planted a tree")

if yes:
    uploaded_file = st.file_uploader("Upload a picture of your task!", type=["jpg", "png", "jpeg"])
    if uploaded_file is not None:
        st.image(uploaded_file)

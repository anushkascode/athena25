import streamlit as st
from PIL import Image 


with open("3_landing.html", "r", encoding = "utf-8") as file:
    html_content = file.read()
st.markdown(html_content, unsafe_allow_html=True)
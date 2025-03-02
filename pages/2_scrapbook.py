import streamlit as st
from PIL import Image

st.title("Page 2: Scrapbook")

if "checkbox1_checked" in st.session_state and st.session_state.checkbox1_checked:
    image = Image.open("assets/tree.png")  # Load the hardcoded image (adjust path if needed)
    st.image(image)
    st.write("Tree Planted!")

if "checkbox2_checked" in st.session_state and st.session_state.checkbox2_checked:
    image = Image.open("assets/thrift.png")  # Load the hardcoded image (adjust path if needed)
    st.image(image)
    st.write("Child Labor Avoided!")
else:
    st.write("Complete sustainable tasks to earn stickers!")

if "page" not in st.session_state:
    st.session_state.page = "1_task.py"
import streamlit as st
from PIL import Image

st.title("Page 2: Scrapbook")

if "checkbox_checked" in st.session_state and st.session_state.checkbox_checked:
    image = Image.open("tree.png")  # Load the hardcoded image (adjust path if needed)
    st.image(image)
    st.write("Tree Planted!")
else:
    st.write("Task not completed on Page 1.")

if st.button("Go to Page 1"):
    st.switch_page("1_task.py")

if "page" not in st.session_state:
    st.session_state.page = "1_task.py"
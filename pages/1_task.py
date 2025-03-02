import streamlit as st
from PIL import Image  # Import Pillow (PIL) for image handling

st.title("Page 1: Task Completion")

if "checkbox_checked" not in st.session_state:
    st.session_state.checkbox_checked = False  # Initialize session state

yes = st.checkbox("Planted a tree")

if yes:
    st.session_state.checkbox_checked = True  # Set session state to True when checked
    image = Image.open("tree.png")  # Load the hardcoded image
    st.image(image)
    st.write("Congratulations!")


    if st.button("Go to Page 2"):
        st.switch_page("pages/2_scrapbook.py")

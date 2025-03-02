import streamlit as st
from PIL import Image  # Import Pillow (PIL) for image handling

st.title("Page 1: Task Completion")

#checkbox 1

if "checkbox1_checked" not in st.session_state:
    st.session_state.checkbox1_checked = False  # Initialize session state

yes1 = st.checkbox("Planted a tree", value=st.session_state.checkbox1_checked)

if yes1:
    st.session_state.checkbox1_checked = True  # Set session state to True when checked
    image_tree = Image.open("tree.png")  # Load the hardcoded image
else:
    st.session_state.checkbox1_checked = False

#checkbox 2

if "checkbox2_checked" not in st.session_state:
    st.session_state.checkbox2_checked = False  # Initialize session state

yes2 = st.checkbox("Shop secondhand", value=st.session_state.checkbox2_checked)

if yes2:
    st.session_state.checkbox2_checked = True  # Set session state to True when checked
    image = Image.open("thrift.png")  # Load the hardcoded image
else:
    st.session_state.checkbox2_checked = False

if st.button("Go to Sticker Book To See Your Progress!"):
    st.switch_page("pages/2_scrapbook.py")
import streamlit as st
from PIL import Image  # Import Pillow (PIL) for image handling

def create_task(label, image_path, session_state_key):
    if session_state_key not in st.session_state:
        st.session_state[session_state_key] = False
    
    checked = st.checkbox(label, value = st.session_state[session_state_key])

    if checked:
        st.session_state[session_state_key] = True
        try:
            Image.open(image_path)
            st.toast("Congratulations! You earned a new sustainability sticker!")
        except FileNotFoundError:
            st.error(f"Image not found: {image_path}")
    else:
        st.session_state[session_state_key] = False

st.title("Page 1: Task Completion")

create_task("Planted a tree", "assets/tree.png","checkbox1_checked") 
create_task("Purchase clothing secondhand", "assets/thrift.png","checkbox2_checked") 
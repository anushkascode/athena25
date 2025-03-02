import streamlit as st
from PIL import Image  # Import Pillow (PIL) for image handling

def create_task(label, image_path, session_state_key, message):
    if session_state_key not in st.session_state:
        st.session_state[session_state_key] = False
    
    checked = st.checkbox(label, value = st.session_state[session_state_key])

    if checked:
        st.session_state[session_state_key] = True
        try:
            Image.open(image_path)
            st.toast("Congratulations! You earned a new sustainability sticker for " + message)
        except FileNotFoundError:
            st.error(f"Image not found: {image_path}")
    else:
        st.session_state[session_state_key] = False

st.title("Page 1: Task Completion")

create_task("Planted a tree", "static/actions-sticker.png","checkbox1_checked", "making a greener world!") 
create_task("Buy clothing secondhand", "static/shopping-sticker.png","checkbox2_checked", "reducing waste!")
create_task("Limit your shower to under 10 minutes", "static/energy-sticker.png", "checkbox3_checked", "saving water!")
create_task("Purchase produce from your local farmer's market", "static/food-sticker.png", "checkbox4_checked", "supporting your community!" )
create_task("Take low-emission transporation", "static/transportation-sticker.png", "checkbox5_checked", "reducing air pollution!")
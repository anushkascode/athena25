import streamlit as st
from PIL import Image  # Import Pillow (PIL) for image handling

def create_task(label, image_path, session_state_key, message, cam_num):
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
        
        uploaded_pic = st.camera_input("Take a pic of your task!", key = cam_num)

        if cam_num not in st.session_state:
            st.session_state[cam_num] = None
        
        if uploaded_pic is not None:
            st.session_state[f"{cam_num}_image"] = uploaded_pic
    
        #if f"{cam_num}_image" in st.session_state:
        #    st.image(st.session_state[f"{cam_num}_image"], caption = "Saved Image", use_column_width = True)
    else:
        st.session_state[session_state_key] = False
    
    


st.title("Complete Your Tasks!")

create_task("Planted a tree", "static/actions-sticker.png","checkbox1_checked", "making a greener world!", "cam1") 
create_task("Buy clothing secondhand", "static/shopping-sticker.png","checkbox2_checked", "reducing waste!", "cam2")
create_task("Limit your shower to under 10 minutes", "static/energy-sticker.png", "checkbox3_checked", "saving water!", "cam3")
create_task("Purchase produce from your local farmer's market", "static/food-sticker.png", "checkbox4_checked", "supporting your community!", "cam4" )
create_task("Take low-emission transporation", "static/transportation-sticker.png", "checkbox5_checked", "reducing air pollution!", "cam5")
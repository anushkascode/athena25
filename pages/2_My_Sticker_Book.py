import streamlit as st
from PIL import Image
from funfact import generate

st.title("Sticker Book")

def show_sticker(label, image_link, cam_num):
    if label in st.session_state and st.session_state[label]:
        image = Image.open(image_link)
                
        st.image(image, width=150)

        if f"{cam_num}_image" in st.session_state:
            uploaded_image = st.session_state[f"{cam_num}_image"]
            st.image(uploaded_image, caption = "Your Task Image", width=150)

        if (label == "checkbox1_checked"):
            task = "Plant a tree"
        elif (label == "checkbox2_checked"):
            task = "Buy Clothing Secondhand"
        elif (label == "checkbox3_checked"):
            task = "Limit your shower to under 10 minutes"
        elif (label == "checkbox4_checked"):
            task = "Purchase Produce from the local Farmer's Market"
        elif (label == "checkbox5_checked"):
            task = "Take Low-emission Transportation"
    
        generate(task)
        with open("fun_fact.txt", "r", encoding="utf-8") as file:
            content = file.read()
        st.write(content)
        
        st.image(image)
        cam_num = st.camera_input("Take a pic of your task!")



col1, col2, col3 = st.columns(3)
with col1:
    show_sticker("checkbox1_checked", "static/actions-sticker.png", "cam1")
    show_sticker("checkbox4_checked", "static/energy-sticker.png", "cam4")
with col2:
    show_sticker("checkbox2_checked", "static/shopping-sticker.png", "cam2")
    show_sticker("checkbox5_checked", "static/transportation-sticker.png", "cam5")
with col3:
    show_sticker("checkbox3_checked", "static/food-sticker.png", "cam3")

st.write("Complete sustainable tasks to earn stickers!")



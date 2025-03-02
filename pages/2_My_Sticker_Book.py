import streamlit as st
from PIL import Image
from funfact import generate

st.title("Sticker Book")

def show_sticker(label, image_link, cam_num):
    if label in st.session_state and st.session_state[label]:
        image = Image.open(image_link)
        st.image(image)
        cam_num = st.camera_input("Take a pic of your task!")
        generate()
        with open("fun_fact.txt", "r", encoding="utf-8") as file:
            content = file.read()
        st.write(content)



col1, col2, col3 = st.columns(3)
with col1:
    show_sticker("checkbox1_checked", "static/actions-sticker.png", "cam1")
    show_sticker("checkbox5_checked", "static/transportation-sticker.png", "cam2")
with col2:
    show_sticker("checkbox2_checked", "static/shopping-sticker.png", "cam3")
    show_sticker("checkbox3_checked", "static/energy-sticker.png", "cam4")
with col3:
    show_sticker("checkbox4_checked", "static/food-sticker.png", "cam5")

st.write("Complete sustainable tasks to earn stickers!")



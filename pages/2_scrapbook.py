import streamlit as st
from PIL import Image

st.title("Page 2: Scrapbook")

def show_sticker(label, image_link):
    if label in st.session_state and st.session_state[label]:
        image = Image.open(image_link)
        st.image(image)

st.write("Complete sustainable tasks to earn stickers!")
show_sticker("checkbox1_checked", "static/actions-sticker.png")
show_sticker("checkbox2_checked", "static/shopping-sticker.png")
show_sticker("checkbox3_checked", "static/energy-sticker.png")
show_sticker("checkbox4_checked", "static/food-sticker.png")
show_sticker("checkbox5_checked", "static/transportation-sticker.png")
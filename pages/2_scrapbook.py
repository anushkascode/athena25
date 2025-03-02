import streamlit as st
from PIL import Image

st.title("Page 2: Scrapbook")

def show_sticker(label, image_link, message):
    if label in st.session_state and st.session_state[label]:
        image = Image.open(image_link)
        st.image(image)
        st.write(message)

st.write("Complete sustainable tasks to earn stickers!")
show_sticker("checkbox1_checked", "static/tree.png", "Tree Planted!")
show_sticker("checkbox2_checked", "static/thrift.png", "Child Labor Avoided!")
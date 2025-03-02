import streamlit as st
from PIL import Image

st.title("Sticker Book")

def show_sticker(label, image_link, cam_num):
    if label in st.session_state and st.session_state[label]:
        image = Image.open(image_link)
        st.image(image, width=150)

        if f"{cam_num}_image" in st.session_state:
            uploaded_image = st.session_state[f"{cam_num}_image"]
            st.image(uploaded_image, caption = "Your Task Image", width=150)


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



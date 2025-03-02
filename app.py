import streamlit as st
import streamlit.components.v1 as components
import base64

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# Dictionary to store base64 encoded images
images = {
    "bbook_logo": encode_image("static/bbook-logo.png"),
    "flower_break": encode_image("static/flower-page-break-black.png"),
    "collage1": encode_image("static/collage1.png"),
    "collage2": encode_image("static/collage2.png"),
}

with open("3_landing.html", "r", encoding="utf-8") as file:
    html_content = file.read()

with open("landing.css", "r", encoding="utf-8") as file:
    css_content = file.read()

# Replace placeholders with actual base64 strings
full_html = f"""
    <style>{css_content}</style>
    {html_content.format(**images)}
"""

components.html(full_html, height=3000, width=1450, scrolling=False)
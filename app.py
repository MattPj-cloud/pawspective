import streamlit as st
import os

st.set_page_config(
    page_title="Pawspective: The Existential Dog Rater",
    page_icon="🐾",
    layout="centered",
)

# Hide Streamlit default chrome for a cleaner look
st.markdown(
    """
    <style>
    #MainMenu, header, footer {visibility: hidden;}
    .stApp {background-color: #0a0e27;}
    iframe {border: none !important;}
    .block-container {padding-top: 1rem !important;}
    </style>
    """,
    unsafe_allow_html=True,
)

html_path = os.path.join(os.path.dirname(__file__), "index.html")
with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

st.components.v1.html(html_content, height=900, scrolling=False)

import pytesseract
from PIL import Image
import io
import streamlit as st


def image_to_text(image_bytes):

    image = Image.open(io.BytesIO(image_bytes))
    text = pytesseract.image_to_string(image)
    return text


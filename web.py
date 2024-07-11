import streamlit as st
from backend import add_centered_text_to_image
from io import BytesIO
from zipfile import ZipFile
import os

st.title("Dodaj Tekst do Obrazu")


howMany = st.number_input("Ile obrazów chcesz przesłać?", min_value=1, max_value=10, value=1, step=1)
size = st.number_input("Rozmiar czcionki", min_value=10, max_value=100, value=30, step=1)

uploaded_images = []
texts = []
output_images = []

for i in range(howMany):
    st.subheader(f"Obraz {i + 1}")

    col1, col2 = st.columns(2)

    with col1:
        image = st.file_uploader(f"Prześlij Obraz {i + 1}", type=["jpg", "jpeg", "png"], key=f"image_uploader_{i}")
        uploaded_images.append(image)

        text = st.text_area(f"Wprowadź tekst dla Obrazu {i + 1}", key=f"text_area_{i}")
        texts.append(text)

    with col2:
        if uploaded_images[i] is not None and texts[i]:
            output_image_path = f"output_image_{i + 1}.png"
            image_with_text = add_centered_text_to_image(uploaded_images[i], texts[i], font_size=size, output_path=output_image_path)
            output_images.append((output_image_path, image_with_text))
            st.image(image_with_text, caption=f"Obraz Wyjściowy {i + 1}", use_column_width=True)

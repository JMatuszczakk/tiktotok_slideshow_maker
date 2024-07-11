import streamlit as st
from backend import add_centered_text_to_image
from io import BytesIO
from zipfile import ZipFile
import os

st.title("Dodaj Tekst do Obrazu")

# Wprowadzenie liczby obrazów
howMany = st.number_input("Ile obrazów chcesz przesłać?", min_value=1, max_value=10, value=1, step=1)
size = st.number_input("Rozmiar czcionki", min_value=10, max_value=100, value=30, step=1)

# Listy do przechowywania danych wejściowych i przetworzonych obrazów
uploaded_images = []
texts = []
output_images = []
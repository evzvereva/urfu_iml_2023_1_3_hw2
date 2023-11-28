import io
import os.path

import streamlit as st
from PIL import Image

from transformers import BlipProcessor, BlipForConditionalGeneration
from translate import Translator


def load_image():
    """
    Функция load_image() позволяет загрузить пользователю изображение и вывести его на экран
    """
    st.header("Классификация изображений")
    uploaded_file = st.file_uploader(label="Выберите изображение для распознавания")

    if uploaded_file is not None:
        image_data = uploaded_file.getvalue()
        st.image(image_data)
        image_data_open = Image.open(io.BytesIO(image_data))
        # Сохранение изображения из буффера
        image_data_open.save("image.png")
        return image_data_open
    else:
        return None


@st.cache_resource
def get_description_image():
    """
    Функция get_description_image() открывает загруженное изображение пользователем и генерирует описание его
    """
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large")

    raw_image = Image.open("image.png")

    text = "a photography of"
    inputs = processor(raw_image, text, return_tensors="pt")

    out = model.generate(**inputs)
    out2 = processor.decode(out[0], skip_special_tokens=True)

    translator = Translator(from_lang="en", to_lang="ru")
    text_rus = translator.translate(out2[0].upper() + out2[1:])
    return text_rus


# Получение полного пути к сохраненному изображению из буффера
file_path = "urfu_iml_2023_1_3_hw2/zvereva_ev/image.png"
absolute_path = os.path.abspath(file_path)


def run_():
    """
    Функция run_() позволяет проверить найдено ли изображение, загруженное пользователем. В случае, если путь к
    изображению найден, запускает функцию get_description_image() для генерации описания.
    """
    try:
        if absolute_path:
            try:
                if st.button("Получить описание изображения"):
                    st.text(get_description_image())
            except:
                st.warning("Загрузите изображение, чтобы получить описание", icon="🚀")
        else:
            exit()
        if "image.png" in absolute_path:
            os.remove("image.png")
    except FileNotFoundError:
        return "Изображение не загружено"


load_image()
run_()

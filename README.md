# Программная инженерия. Практическое задание №3

Приложение разработано с использованием фреймворка [Streamlit](https://streamlit.io/).

## Используемая модель
- Классификация и описание изображений. Модель описания изображения [Salesforce/blip-image-captioning-large](https://huggingface.co/Salesforce/blip-image-captioning-large)

## Как запустить
Запуск осуществляется через модуль streamlit:
```
streamlit run get_description_image.py
```

### Описание изображения
Необходимо выбрать изображение и нажать кнопку "Получить описание изображения". В результате появится текстовое описание изображения на русском языке.

![Результат работы моделей "Классификации и описания изображений"](https://raw.githubusercontent.com/kavlab/urfu_iml_2023_1_3_hw2/main/zvereva_ev/image_result.jpg)



import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

API = "my-api-key"

genai.configure(api_key=API)


model = genai.GenerativeModel(model_name='gemini-1.5-flash')
def get_gemini_resposne(input, image):
    if input != "":
        response = model.generate_content([input,image])
    else:
        response = model.generate_content(image)
    return response.text



st.set_page_config(page_title="Image Captioning")
st.header('Image Captioning Application')
input = ("Generate a caption of about 15 words for the following image.")
uploaded_file = st.file_uploader("Choose an image : ", type=['jpg', 'jpeg', 'png'])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)


submit = st.button("Generate Caption")


if submit :
    response = get_gemini_resposne(input, image)
    st.subheader("Generated Caption...")
    st.write(response)
#%%
import streamlit as st 
import os 
import requests 
import json 
from dotenv import load_dotenv
import os

# Access the variables
project_name = os.getenv("PROJECT_NAME")

def main():
    st.set_page_config(
        page_title= project_name,
        page_icon=":whale:",
        initial_sidebar_state="auto"
        ) 

    st.title(project_name)
    _help = 'Something as a helper text'

    label = 'Select Something'

    _ocrtype = st.radio(label = label,
                            options = ['Paddle OCR', 'TesseractOCR', 'Google API'],
                            horizontal=True,
                            index=None,
                            help = _help)
    st.write('You selected: ', _ocrtype)

    interest_rate  = st.slider("Pick a number", 0, 100, key='interest_rate')
    principal_amount = st.slider("Pick a number", 0, 100, key='principal_amount')

    st.write('interest_rate', interest_rate)


if __name__ == '__main__':
    main()
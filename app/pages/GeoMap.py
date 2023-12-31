import os.path

import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(page_title="Maps",page_icon=":earth_africa:",layout="wide")
st.title("Geo Map Page")
st.sidebar.title("Map page")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


def get_data():
    data_path = os.path.join(os.path.dirname(__file__),'..','data','clean_data.csv')
    cancer_data = pd.read_csv(data_path)
    coordinates = cancer_data[['Longitude','Latitude']]
    coordinates['lat'] = coordinates['Latitude']
    coordinates['lon'] = coordinates['Longitude']
    coordinates['gender'] = cancer_data['Patient\'s Gender']
    return coordinates


if 'df' not in st.session_state:
    st.session_state.df = get_data()
df = st.session_state.df

with st.form("my_form"):
    header = st.columns([1, 2, 2])
    header[0].subheader('Color')
    header[1].subheader('Opacity')
    header[2].subheader('Size')

    row1 = st.columns([1, 2, 2])
    colorA = row1[0].color_picker('Male', '#0000FF')
    opacityA = row1[1].slider('A opacity', 20, 100, 50, label_visibility='hidden')
    sizeA = row1[2].slider('A size', 50, 200, 100, step=10, label_visibility='hidden')

    row2 = st.columns([1, 2, 2])
    colorB = row2[0].color_picker('Female', '#FF0000')
    opacityB = row2[1].slider('B opacity', 20, 100, 50, label_visibility='hidden')
    sizeB = row2[2].slider('B size', 50, 200, 100, step=10, label_visibility='hidden')

    st.form_submit_button('Update map')

alphaA = int(opacityA * 255 / 100)
alphaB = int(opacityB * 255 / 100)

df['color'] = np.where(df.gender == '1', colorA + f'{alphaA:02x}', colorB + f'{alphaB:02x}')
df['size'] = np.where(df.gender == '1', sizeA, sizeB)

st.map(df, size='size', color='color')

import os

import pandas as pd
import streamlit as st

st.set_page_config(page_title="Tables", page_icon=":spiral_calendar_pad:", layout="wide")
st.title("Patients' Metadata")
st.sidebar.title("Filters goes here")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


# path = os.path.join(os.path.dirname(__file__), '..', 'data', 'clean_data.csv')
# data = pd.read_csv(path)
# st.write(data)

# data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'clean_data.csv')
# data_frame = pd.read_csv(data_path)
# # st.dataframe(data_frame)
#
# # Display a paginated version of the Dataframe
# page_size = st.slider("Rows per page", min_value=1, max_value=len(data_frame), value=3)
# current_page = st.slider("Page", min_value=1, max_value=(len(data_frame) // page_size) + 1, value=1)
# start_idx = (current_page - 1) * page_size
# end_idx = start_idx + page_size
# st.write(data_frame[start_idx:end_idx])


def load_patient_metadata():
    data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'clean_data.csv')
    data_frame = pd.read_csv(data_path)
    st.write(data_frame)

    # Display a paginated version of the Dataframe
    page_size = st.slider("Rows per page", min_value=1, max_value=len(data_frame), value=3)
    current_page = st.slider("Page", min_value=1, max_value=(len(data_frame) // page_size) + 1, value=1)
    start_idx = (current_page - 1) * page_size
    end_idx = start_idx + page_size
    st.dataframe(data_frame[start_idx:end_idx])


load_patient_metadata()

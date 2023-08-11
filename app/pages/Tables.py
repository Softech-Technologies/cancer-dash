import pandas
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Tables", page_icon=":spiral_calendar_pad:", layout="wide")
st.title("Cancer Dashboard")
st.write("This is a cancer dashboard table")
st.sidebar.title("Filters goes here")
st.markdown("Ata mimi na gamble tu")

data = pandas.read_csv()

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
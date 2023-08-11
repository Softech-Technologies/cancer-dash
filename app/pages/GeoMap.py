import streamlit as st

st.set_page_config(page_title="Maps",page_icon=":earth_africa:",layout="wide")
st.title("Geo Map Page")
st.write("This is a cancer dashboard for data exploration")
st.sidebar.title("Map page")
st.markdown("This is a cancer dashboard for data visualization and exploitations")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
import streamlit as st

st.set_page_config(page_title="Charts",page_icon=":chart_with_upwards_trend:",layout="wide")
st.title("Graphs Page")
st.write("This is a cancer dashboard for data exploration")
st.sidebar.title("Main page")
st.markdown("This is a cancer dashboard for data visualization and exploitations")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
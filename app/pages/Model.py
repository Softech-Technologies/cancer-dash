import streamlit as st

st.set_page_config(page_title='Predictive Model', page_icon=':hospital:', layout='wide')
st.title('Prediction Model')

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


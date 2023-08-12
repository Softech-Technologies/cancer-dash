import os

import pandas as pd
import streamlit as st
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

st.set_page_config(page_title='Predictive Model', page_icon=':hospital:', layout='wide')
st.title('Prediction Model')

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'clean_data.csv')
data_frame = pd.read_csv(data_path)


def build_form():
    # User input form
    with st.form("User Information"):
        latitude = st.number_input("Latitude", value=0.0,step=0.01)
        longitude = st.number_input("Longitude", value=0.0,step=0.01)
        age = st.number_input("Age", min_value=0, max_value=100, value=20)
        any_condition = st.selectbox("Any Pre-existing conditions", ["Yes", "No"])
        gender = st.selectbox("Gender", ["Male", "Female"])
        marital_status = data_frame["Marital Status"].unique().tolist()
        marriage_status = st.selectbox("Marital Status", marital_status)

        submitted = st.form_submit_button("Submit")

    # Display user input
    if submitted:
        st.write("User Information:")
        st.write(f"Any Pre-existing condition: {any_condition}")
        st.write(f"Gender: {gender}")
        st.write(f"Marital status: {marriage_status}")

        data = {
            "Latitude": latitude,
            "Longitude": longitude,
            "Patient\'s Age": age,
            "Patient\'s Gender": gender,
            "Any Pre-existing condition": any_condition,
            "Marital Status": marriage_status
        }

        if any_condition == "Yes":
            data['Any Pre-existing condition'] = 1
        else:
            data['Any Pre-existing condition'] = 2
        if gender == "Male":
            data['Patient\'s Gender'] = 1
        else:
            data['Patient\'s Gender'] = 2

        if marital_status == "Married_Mono":
            data['Marital Status'] = 1
        elif marital_status == "Single":
            data['Marital Status'] = 2
        elif marital_status == "Widowed":
            data['Marital Status'] = 3
        elif marital_status == "Married_Poly":
            data['Marital Status'] = 4
        elif marital_status == "Unknown":
            data['Marital Status'] = 5
        elif marital_status == "Other":
            data['Marital Status'] = 6
        elif marital_status == "Separated":
            data['Marital Status'] = 7
        elif marital_status == "Divorced":
            data['Marital Status'] = 8
        else:
            data['Marital Status'] = 2
        # data["Any Pre-existing condition"] = data["Any Pre-existing condition"].map({"Yes": 1, "No": 0})
        # data["Marital Status"] = data["Marital Status"].map({"Married_Mono": 1, "Single": 2, "Widowed": 3, "Married_Poly": 4, "Unknown": 5, "Other": 6, "Separated": 7, "Divorced": 8})
        # data["Patient's Gender"] = data["Patient's Gender"].map({"Male": 1, "Female": 2})

        prediction = prediction_model(data)
        st.write("Probability of getting cancer are: \n")
        st.write("Chances")
        st.write(prediction["prediction"])
        st.write("Accuracy")
        st.write(prediction["accuracy"])


def prediction_model(data_row):
    m_data = data_frame.copy()
    m_data["Any Pre-existing condition"] = m_data["Any Pre-existing condition"].map({"Yes": 1, "No": 0})
    m_data["Marital Status"] = m_data["Marital Status"].map({"Married_Mono": 1, "Single": 2, "Widowed": 3, "Married_Poly": 4, "Unknown": 5, "Other": 6, "Separated": 7, "Divorced": 8})
    m_data["Patient\'s Gender"] = m_data["Patient\'s Gender"].map({"Male": 1, "Female": 2})
    m_data["Status"] = m_data["Status"].map({"Alive": 0, "Dead": 1})
    m_data.dropna(axis=1)
    X = m_data.drop(["Status", "Ward", "Patient's Occupation", "Type of Cancer", "Initial diagnosis", "Final diagnosis", "Treatment Received", "Other treatment", "Year died"], axis=1)
    y = m_data["Status"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    # Classifier
    rf_classifier = HistGradientBoostingClassifier("log_loss", random_state=42)
    rf_classifier.fit(X_train, y_train)
    y_pred = rf_classifier.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    frame = pd.DataFrame([data_row])
    pred = rf_classifier.predict(frame)
    print(pred[0])
    acc = accuracy * 100
    pred = dict(accuracy=acc, prediction=pred[0])
    return pred


build_form()

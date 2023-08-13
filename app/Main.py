import streamlit as st

st.set_page_config(page_title="Main Page",page_icon=":house:",layout="wide")
st.title("Information Page")
st.sidebar.title("Main page")
st.markdown("This is a cancer dashboard for data visualization and exploration")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.title("Facts about cancer in Kenya")
st.markdown(
"Cancer is a significant public health concern in Kenya, as it is in many parts of the world. Here are some key points about cancer in Kenya:\n"

"1. **Prevalence:** Cancer is one of the leading causes of morbidity and mortality in Kenya. The incidence of cancer has been increasing over the years due to various factors including lifestyle changes, population growth, and increased awareness.\n"

"2. **Common Types:** The most common types of cancer in Kenya include cervical cancer, breast cancer, prostate cancer, esophageal cancer, and colorectal cancer. Cervical cancer is particularly prevalent and is a major concern in women's health.\n"

"3. **Risk Factors:** Risk factors for cancer in Kenya are similar to those in other parts of the world. These include tobacco use, excessive alcohol consumption, unhealthy diets, lack of physical activity, exposure to certain chemicals and pollutants, infections (such as Human Papillomavirus for cervical cancer), and genetic predisposition.\n"

"4. **Healthcare Infrastructure:** Access to quality healthcare, including cancer screening, diagnosis, and treatment, can be challenging for many Kenyans due to factors like limited resources, geographical disparities, and inadequate health infrastructure in some regions.\n"

"5. **Awareness and Education:** Efforts to raise awareness about cancer prevention, early detection, and available treatments are ongoing in Kenya. Organizations and government agencies conduct campaigns to educate the public about risk factors and the importance of regular screenings.\n"

"6. **Screening and Detection:** Screening for cancer, especially for common types like cervical and breast cancer, is crucial for early detection and improved outcomes. However, there are challenges in implementing widespread screening programs due to resource limitations.\n"

"7. **Treatment:** Cancer treatment options in Kenya include surgery, chemotherapy, radiation therapy, and palliative care. Access to advanced treatments and medications can be limited in certain areas, leading some patients to seek treatment abroad.\n"

"8. **Support Organizations:** There are various non-governmental organizations and support groups in Kenya that focus on cancer awareness, patient support, and advocacy for better cancer care.\n"

"9. **Government Initiatives:** The Kenyan government has taken steps to address cancer as a public health issue. For instance, the Ministry of Health has developed guidelines for cancer management and control, and some cancer treatments are subsidized in government hospitals.\n"

"10. **Research and Data:** Collecting accurate data on cancer incidence, prevalence, and mortality is essential for effective planning and resource allocation. Various research initiatives and collaborations are working to improve the understanding of cancer patterns in Kenya.\n"

)

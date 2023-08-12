import os.path
import warnings

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st
from sklearn import datasets

st.set_page_config(page_title="Charts", page_icon=":chart_with_upwards_trend:", layout="wide")
st.set_option('deprecation.showPyplotGlobalUse', False)
st.title("Graphs Page")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

warnings.filterwarnings("ignore")

####### Load Dataset #####################

breast_cancer = datasets.load_breast_cancer(as_frame=True)

breast_cancer_df = pd.concat((breast_cancer["data"], breast_cancer["target"]), axis=1)

breast_cancer_df["target"] = [breast_cancer.target_names[val] for val in breast_cancer_df["target"]]

########################################################

# st.set_page_config(layout="wide")

st.markdown("## Cancer Dataset Analysis")  ## Main Title

################# Scatter Chart Logic #################

st.sidebar.markdown("### Scatter Chart: Explore Relationship Between Measurements :")

measurements = breast_cancer_df.drop(labels=["target"], axis=1).columns.tolist()

x_axis = st.sidebar.selectbox("X-Axis", measurements)
y_axis = st.sidebar.selectbox("Y-Axis", measurements, index=1)

if x_axis and y_axis:
    scatter_fig = plt.figure(figsize=(6, 4))

    scatter_ax = scatter_fig.add_subplot(111)

    malignant_df = breast_cancer_df[breast_cancer_df["target"] == "malignant"]
    benign_df = breast_cancer_df[breast_cancer_df["target"] == "benign"]

    malignant_df.plot.scatter(x=x_axis, y=y_axis, s=120, c="tomato", alpha=0.6, ax=scatter_ax, label="Malignant")
    benign_df.plot.scatter(x=x_axis, y=y_axis, s=120, c="dodgerblue", alpha=0.6, ax=scatter_ax,
                           title="{} vs {}".format(x_axis.capitalize(), y_axis.capitalize()), label="Benign");

########## Bar Chart Logic ##################

st.sidebar.markdown("### Bar Chart: Average Measurements Per Tumor Type : ")

avg_breast_cancer_df = breast_cancer_df.groupby("target").mean()
bar_axis = st.sidebar.multiselect(label="Average Measures per Tumor Type Bar Chart",
                                  options=measurements,
                                  default=["mean radius", "mean texture", "mean perimeter", "area error"])

if bar_axis:
    bar_fig = plt.figure(figsize=(6, 4))

    bar_ax = bar_fig.add_subplot(111)

    sub_avg_breast_cancer_df = avg_breast_cancer_df[bar_axis]

    sub_avg_breast_cancer_df.plot.bar(alpha=0.8, ax=bar_ax, title="Average Measurements per Tumor Type");

else:
    bar_fig = plt.figure(figsize=(6, 4))

    bar_ax = bar_fig.add_subplot(111)

    sub_avg_breast_cancer_df = avg_breast_cancer_df[["mean radius", "mean texture", "mean perimeter", "area error"]]

    sub_avg_breast_cancer_df.plot.bar(alpha=0.8, ax=bar_ax, title="Average Measurements per Tumor Type");

st.sidebar.markdown("### Histogram: Explore Distribution of Measurements : ")

################# Histogram Logic ########################
hist_axis = st.sidebar.multiselect(label="Histogram Ingredient", options=measurements, default=["mean radius", "mean texture"])
bins = st.sidebar.radio(label="Bins :", options=[10, 20, 30, 40, 50], index=4)

if hist_axis:
    hist_fig = plt.figure(figsize=(6, 4))

    hist_ax = hist_fig.add_subplot(111)

    sub_breast_cancer_df = breast_cancer_df[hist_axis]

    sub_breast_cancer_df.plot.hist(bins=bins, alpha=0.7, ax=hist_ax, title="Distribution of Measurements");
else:
    hist_fig = plt.figure(figsize=(6, 4))

    hist_ax = hist_fig.add_subplot(111)

    sub_breast_cancer_df = breast_cancer_df[["mean radius", "mean texture"]]

    sub_breast_cancer_df.plot.hist(bins=bins, alpha=0.7, ax=hist_ax, title="Distribution of Measurements");

#################### Hexbin Chart Logic ##################################

st.sidebar.markdown("### Hexbin Chart: Explore Concentration of Measurements :")

hexbin_x_axis = st.sidebar.selectbox("Hexbin-X-Axis", measurements, index=0)
hexbin_y_axis = st.sidebar.selectbox("Hexbin-Y-Axis", measurements, index=1)

if hexbin_x_axis and hexbin_y_axis:
    hexbin_fig = plt.figure(figsize=(6, 4))

    hexbin_ax = hexbin_fig.add_subplot(111)

    breast_cancer_df.plot.hexbin(x=hexbin_x_axis, y=hexbin_y_axis,
                                 reduce_C_function=np.mean,
                                 gridsize=25,
                                 # cmap="Greens",
                                 ax=hexbin_ax, title="Concentration of Measurements");

##################### Plot ages ################################

data_url = os.path.join(os.path.dirname(__file__),'..','data','clean_data.csv')
data_frame = pd.read_csv(data_url)
st.write("Age distribution:")
plt.figure(figsize=(5,4))
ages = data_frame['Patient\'s Age'].plot(kind="density",color="r")
plt.xlabel('Patient\'s Age')
plt.ylabel('Count')
plt.title('Patient\'s Age vs Count')
plt.show()
st.pyplot(plt)

############## Pie chart ##########################
# plt.title("Gender distribution")
# pie = data_frame["Patient's Gender"].value_counts().plot(kind='pie', autopct='%1.1f%%', shadow=True, startangle=90)
# # plt.show()
# st.pyplot(pie)
genders = data_frame['Patient\'s Gender'].value_counts()
labels = data_frame['Patient\'s Gender'].unique()

st.write("Gender distribution:")
fig, ax = plt.subplots()
ax.pie(genders, labels=labels, autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
st.pyplot(fig)

st.write("Breast cancer Detail Analysis")

# st.sidebar.markdown("### Bar Chart: Average Measurements Per Tumor Type : ")
#
# avg_breast_cancer_df = breast_cancer_df.groupby("target").mean()
# barf_axis = st.sidebar.multiselect(label="Average Measures per Tumor Type Bar Chart 1",
#                                    options=measurements,
#                                    default=["mean radius", "mean texture", "mean perimeter", "area error"])
#
# if bar_axis:
#     barf = plt.figure(figsize=(6, 4))
#
#     barf_ax = barf.add_subplot(111)
#
#     sub_avg_breast_cancer_df = avg_breast_cancer_df[barf_axis]
#
#     sub_avg_breast_cancer_df.plot.bar(alpha=0.8, ax=barf_ax, title="Average Measurements per Tumor Type");
#
# else:
#     barf_fig = plt.figure(figsize=(6, 4))
#
#     barf_ax = bar_fig.add_subplot(111)
#
#     sub_avg_breast_cancer_df = avg_breast_cancer_df[["mean radius", "mean texture", "mean perimeter", "area error"]]
#
#     sub_avg_breast_cancer_df.plot.bar(alpha=0.8, ax=barf_ax, title="Average Measurements per Tumor Type");
##################### Layout Application ##################

container1 = st.container()
col1, col2 = st.columns(2)

with container1:
    with col1:
        scatter_fig
    with col2:
        bar_fig

container2 = st.container()
col3, col4 = st.columns(2)

with container2:
    with col3:
        hist_fig
    with col4:
        hexbin_fig

container3 = st.container()
col5, col6 = st.columns(2)
# with container3:
#     with col5:


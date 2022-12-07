import time
import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Real-Time Data Science Dashboard",
    page_icon="✅",
    layout='wide',
)

dataset_url = "https://raw.githubusercontent.com/subaash1112/Assured-Data-Science-FS/data/property2.csv"


# read csv from a url
@st.experimental_memo
def get_data() -> pd.DataFrame:
    return pd.read_csv(dataset_url)


df = get_data()

# dashboard title
st.title("Real-Time / Live Data Science Dashboard")

# top-level filters
location_filter = st.selectbox('Select the location', pd.unique(df["Location"]))

# dataframe filter
df = df[df['Location'] == location_filter]

# Properties/summary cards
# create three columns
p1, p2, p3 = st.columns(3)

# fill in those three columns with respective inputs

# p1.metric(
#     label = ""
# )

# create two columns for charts

fig_col1, fig_col2 = st.columns(2)

with fig_col1:
    st.markdown('### First Chart')
    fig = px.density_heatmap(data_frame=df, y="Location", x='Price')
    st.write(fig)

with fig_col2:
    st.markdown('### Second Chart')
    fig2 = px.histogram(data_frame=df, x='Price')
    st.write(fig2)

# Data table

st.dataframe(df)

# for seconds in range(200):
#     df['Price'] = df[]

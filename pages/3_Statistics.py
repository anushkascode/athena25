import streamlit as st
from PIL import Image 
import pandas as pd

st.title("Page 3: Data Analytics")
# zip = st.number_input("What is your zipcode?")

sdr_data = pd.read_csv("data/sdr_data.csv")
st.bar_chart(sdr_data)

#urban_data = pd.read_csv("data/global_urbanization_climate_metrics.csv")
#st.pyplot(urban_data)

# data3 = pd.read_csv("data3.csv")
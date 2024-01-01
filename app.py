import streamlit as st
from prediction_page import show_prediction_page
from analysis_page import show_analysis_page


page = st.sidebar.selectbox("Explore Or Predict", ("Predict", "Explore"))

if page == "Predict":
    show_prediction_page()
else:
    show_analysis_page()
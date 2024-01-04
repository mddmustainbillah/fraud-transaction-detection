import streamlit as st
from prediction_page import show_prediction_page
from analysis_page import show_analysis_page
from overview import overview_page



# Use radio buttons for Explore or Predict
page = st.sidebar.radio("Pages", ("Overview","Analysis", "Predict"))

if page == "Overview":
    overview_page()
elif page == "Predict":
    show_prediction_page()
else:
    show_analysis_page()
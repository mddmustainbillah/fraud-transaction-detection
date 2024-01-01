import streamlit as st
import numpy as np

def show_prediction_page():
    st.header("Welcome to Prediction Page")


    distance_from_home = st.text_input("The distance from home where the transaction happened (km)", '')
    distance_from_last_transaction = st.text_input("The distance from last transaction happened (km)", '') 
    ratio_to_median_purchase_price = st.text_input("Ratio to median purchase price (between 0 to 300)", '') 
    # repeat_retailer = st.radio("Is the transaction happened from same retailer?", [0,1])
    # used_chip = st.radio("Is the transaction through chip (credit card)?", [0,1])
    # used_pin_number = st.radio("Is the transaction happened by using PIN number?", [0,1])
    # online_order = st.radio("Is the transaction an online order?", [0,1])

    # Frontend code
    mapping = {"Yes": 1, "No": 0}

    repeat_retailer = st.radio("Is the transaction happened from same retailer?", list(mapping.keys()))
    repeat_retailer = mapping[repeat_retailer]
    # st.write(repeat_retailer)

    used_chip = st.radio("Is the transaction through chip (credit card)?", list(mapping.keys()))
    used_chip = mapping[used_chip]
    # st.write(used_chip)

    used_pin_number = st.radio("Is the transaction happened by using PIN number?", list(mapping.keys()))
    used_pin_number = mapping[used_pin_number]
    # st.write(used_pin_number)


    online_order = st.radio("Is the transaction an online order?", list(mapping.keys()))
    online_order = mapping[online_order]
    # st.write(online_order)


    ok = st.button("Predict")
    if ok:
        row = np.array([distance_from_home, distance_from_last_transaction, ratio_to_median_purchase_price, repeat_retailer, used_chip, used_pin_number, online_order]) 
        st.write(row)

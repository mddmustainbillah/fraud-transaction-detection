import streamlit as st
import pandas as pd
import plotly.express as px

def show_analysis_page():
    st.header(":chart: Welcome to Analysis Page")

    df = pd.read_csv("data/fraud_data.csv")
    st.write(df.head())




    st.subheader('Distance_from_home:')
    st.write("Fraud Transactions: The average distance_from_home for fraud transactions is significantly higher (65.56) compared to non-fraud transactions (22.96). This indicates that a majority of fraud transactions tend to occur at greater distances from the home location.")
    st.write("Non-Fraud Transactions: Non-fraud transactions, on the other hand, have a lower average distance_from_home, suggesting that these transactions are more likely to occur closer to the cardholder's home.")
     
    st.subheader("Distance_from_last_transaction:")
    st.write("Fraud Transactions: The average distance_from_last_transaction for fraud transactions is higher (12.56) compared to non-fraud transactions (4.30). This could indicate that fraud transactions are less frequent and occur with larger spatial gaps between consecutive transactions.")
    st.write("Non-Fraud Transactions: Non-fraud transactions have a lower average distance_from_last_transaction, suggesting that these transactions are more likely to be closer in time and space.")
    
    st.subheader("Ratio_to_median_purchase_price:")

    st.write("Fraud Transactions: The average ratio_to_median_purchase_price for fraud transactions is substantially higher (6.01) than for non-fraud transactions (1.43). This may indicate that fraud transactions involve purchases with higher ratios compared to the median, possibly pointing to anomalous spending behavior.")
    st.write("Non-Fraud Transactions: Non-fraud transactions have a lower average ratio_to_median_purchase_price, suggesting more typical spending patterns.")
    st.subheader("Repeat_Retailer, Used_Chip, Used_Pin_Number, Online_Order:")

    st.write("Fraud Transactions: These features show relatively consistent patterns between fraud and non-fraud transactions. For example, both fraud and non-fraud transactions tend to involve repeat retailers, use a chip, and have online orders.")
    st.write("Non-Fraud Transactions: Similar characteristics are observed in non-fraud transactions, indicating that these features may not be strong indicators of fraud on their own.")
    st.subheader("Additional Observations:")

    st.write("The standard deviation for distance_from_home is much higher in fraud transactions, indicating greater variability in the distances for fraudulent activities.")
    st.write("The minimum and maximum values for distance_from_home, distance_from_last_transaction, and ratio_to_median_purchase_price are considerably higher for fraud transactions, showcasing the presence of extreme values in fraudulent activities.")
    st.subheader("Overall Comparison:")

    st.write("Fraud transactions exhibit more variability and extreme values across multiple features, reflecting the diverse tactics used by fraudsters.")
    st.write("Non-fraud transactions tend to follow more standardized patterns, with lower variability in the analyzed features.")
    st.write("These observations provide a comprehensive understanding of the differences between fraud and non-fraud transactions, emphasizing the importance of considering multiple features in fraud detection models. Further exploration and feature engineering may be needed to enhance the effectiveness of fraud detection algorithms.'")




################################################################
#           Fraud distribution (pie chart)
################################################################
    # Map labels for the legend
    legend_labels = {0.0: 'Not Fraud', 1.0: 'Fraud'}
    df['fraud_label'] = df['fraud'].map(legend_labels)

    # Streamlit app
    st.title("Fraud Distribution Pie Chart")

    # Create a pie chart using Plotly Express with custom labels
    fig = px.pie(df, names='fraud_label', hole=0.4)

    # Show the pie chart in the Streamlit app
    st.plotly_chart(fig)


################################################################
    
################################################################



    # # Streamlit app
    # st.title("Distance from Home Distribution by Fraud Category")

    # # Create a grouped histogram using Plotly Express
    # fig = px.histogram(df, x='distance_from_home', color='fraud_label', nbins=30, title='Distance from Home Distribution by Fraud Category')

    # # Show the histogram in the Streamlit app
    # st.plotly_chart(fig)






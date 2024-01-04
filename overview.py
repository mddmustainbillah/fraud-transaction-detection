import streamlit as st

st.set_page_config(page_title="Fraud Detection", page_icon=":bar_chart:",layout="wide")

def overview_page():


    st.markdown('<style>div.block-container{padding-top:1rem; text-align:justify;}</style>', unsafe_allow_html=True)

    st.header("Project Title: Automated Fraud Transaction Detection System")

    st.subheader("Overview:")
    st.write("In a world dominated by digital transactions, the need for robust fraud detection systems is paramount. The 'Automated Fraud Transaction Detection System' is a comprehensive end-to-end project designed to address the evolving challenges in the realm of digital payments. With a focus on both Card-Present and Card-Not-Present transactions, this project harnesses the power of machine learning to identify and prevent fraudulent activities.")

    st.subheader("Objective:")
    st.write("The primary objective of this project is to create a production-level fraud detection system capable of handling large volumes of digital transactions. By leveraging a modular coding approach, the system seamlessly ingests, validates, transforms, trains machine learning models, evaluates their performance, and provides real-time predictions, making it a valuable asset for stakeholders in the financial sector.")

    st.subheader("Dataset:")
    st.write("The dataset used in this project was sourced from Kaggle, a leading platform for data science competitions. The data reflects the challenges posed by the digital landscape, with millions of records being stolen daily. The project tackles the complexities associated with the vast number of daily card transactions, aiming to enhance fraud detection capabilities.")
    
    st.subheader("Feature Explanation:")

    st.write("distance_from_home - the distance from home where the transaction happened.")
    st.write("distance_from_last_transaction - the distance from last transaction happened.")
    st.write("ratio_to_median_purchase_price - Ratio of purchased price transaction to median purchase price.")
    st.write("repeat_retailer - Is the transaction happened from same retiler.")
    st.write("used_chip - Is the transaction through chip (credit card).")
    st.write("used_pin_number - Is the transaction happened by using PIN number.")
    st.write("online_order - Is the transaction an online order.")
    st.write("fraud - Is the transaction fraudulent.")



    st.subheader("Key Features:")

    st.write("Automation: The project is fully automated, ensuring a streamlined workflow from data ingestion to model prediction. This automation allows for efficient handling of large-scale data without manual intervention.")

    st.write("User Interaction: The system incorporates a user-friendly web interface, enabling users to input data for prediction and explore detailed analyses of the dataset. This interactive feature enhances accessibility and usability.")

    st.write("Modular Coding: The project employs modular coding principles, enhancing code readability, maintainability, and scalability. Each step in the workflow is encapsulated in modular components, facilitating easy updates and modifications.")

    st.write("Machine Learning Model: The heart of the system is a machine learning model trained on the provided dataset. The model employs advanced techniques to discern patterns and anomalies, providing accurate fraud predictions.")

    st.subheader("Challenges:")
    st.write("In a landscape where cyber threats continually evolve, the detection of fraud presents ongoing challenges. The project addresses these challenges by utilizing state-of-the-art techniques and staying adaptive to emerging trends in digital payment security.")

    st.subheader("Outcome:")
    st.write("The Automated Fraud Transaction Detection System is a testament to the fusion of technology and data science in fortifying digital payment ecosystems. Its production-level capabilities, user-friendly interface, and effective fraud detection make it a valuable asset for financial institutions aiming to secure their transactions.")

    st.subheader("Future Enhancements:")
    st.write("Future iterations of the project may include the integration of additional data sources, continuous model training for adaptive learning, and the exploration of advanced anomaly detection algorithms to stay ahead of emerging fraud patterns.")

    st.subheader("Conclusion:")
    st.write("The Automated Fraud Transaction Detection System stands as a beacon of innovation, showcasing the power of data science in securing digital transactions. Its modular architecture, coupled with automation and user interaction, positions it as a versatile solution in the ongoing battle against cyber threats in the financial domain.")





import streamlit as st
from PIL import Image


def show_home_page():
    col1, col2 = st.columns([0.2, 0.8])
    
    with col1:
        st.image(Image.open("logo.png"), use_column_width=True)
    
    with col2:
        st.title("EduSustain")
    st.write("Welcome to our application! We help predict the success or dropout status of students based on user inputs.")
    st.write("Using this application, educators and administrators can identify students who may be at risk and take appropriate actions to support them.")
    st.write("To get started, navigate to the 'Predict' section and provide the required information. Our predictive model will then generate the outcome.")

    st.subheader("Instructions:")
    st.write("1. Go to the 'Predict' section.")
    st.write("2. Enter the necessary details about the student.")
    st.write("3. Click on the 'Predict' button to obtain the predicted outcome.")
    st.write("4. Explore the 'Explore' section for more insights and analysis.")
    st.write("4. Click on the 'Contact' section for more informations about our team.")
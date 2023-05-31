import streamlit as st
from PIL import Image

def show_contact_page():
    st.title("Contact")
    st.write("For any inquiries, feedback, or support, please feel free to reach out to us.")

    st.subheader("Contact Information")
    st.write("Email: edusustain@gmail.com ![Email Icon](https://img.icons8.com/small/16/000000/email.png)")
    st.write("Phone: +216 956868714 ![Phone Icon](https://img.icons8.com/small/16/000000/phone.png)")

    st.subheader("Feedback")
    st.write("We value your feedback! Please provide your suggestions, report issues, or share your experience using our application through our feedback form ")

    st.subheader("Frequently Asked Questions (FAQ)")

    st.write("Welcome to the Frequently Asked Questions section. Here are some common questions and answers about our application.")

    # Question 1
    st.subheader("Q: What is the purpose of this application?")
    st.write("A: The purpose of this application is to predict the success or dropout status of a student based on user inputs.")

    # Question 2
    st.subheader("Q: How accurate are the predictions?")
    st.write("A: The accuracy of the predictions depends on various factors, including the quality of the input data and the machine learning model used. We strive to provide accurate predictions, but it's important to note that no prediction is 100% guaranteed.")

    # Question 3
    st.subheader("Q: What features are considered for prediction?")
    st.write("A: The prediction model takes into account various features such as student demographics, academic performance, socioeconomic factors, and more. The specific features used may vary depending on the model and dataset.")

    # Question 4
    st.subheader("Q: How can I use this application?")
    st.write("A: To use this application, navigate to the 'Predict' section and provide the required inputs. The application will then generate a prediction on the success or dropout status of the student.")

    # Question 5
    st.subheader("Q: Can I explore the dataset used for training?")
    st.write("A: Yes, you can explore the dataset used for training in the 'Explore' section of the application. It provides insights and visualizations to help you gain a better understanding of the data.")

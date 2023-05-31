import streamlit as st

def show_feedback_page():
    st.title("Feedback")

    st.write("We value your feedback! Please provide your suggestions, report issues, or share your experience using our application.")

    st.subheader("Feedback Form")

    # Create input fields for user's name, email, and feedback message
    name = st.text_input("Name")
    email = st.text_input("Email")
    feedback_message = st.text_area("Feedback")

    # Create a button to submit the feedback
    if st.button("Submit"):
        # Save the feedback to a database or send it via email
        # You can customize this code to meet your specific requirements

        # Example: Print the feedback message
        st.write(f"Thank you for your feedback, {name}!")
        st.write("We have received your feedback")
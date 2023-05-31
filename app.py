import streamlit as st
from streamlit_option_menu import option_menu
from predict_page import show_predict_page
from home_page import show_home_page
from contact_page import show_contact_page
from feedback_page import show_feedback_page

#page = st.sidebar.selectbox("Explore Or Predict", ("Predict", "Explore"))
selected = option_menu(
    menu_title=None,
    options=["Home","Predict","Explore","Contact","Feedback"],
    icons = ["house", "search", "book", "envelope","envelope-paper"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
)
if selected == "Home":
    show_home_page()
elif selected == "Predict":
    show_predict_page()
elif selected == "Contact":
    show_contact_page()
elif selected == "Feedback":
    show_feedback_page()
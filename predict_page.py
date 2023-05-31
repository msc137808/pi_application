import streamlit as st
import pickle

with open('data.pkl_unique', 'rb') as file:
    model = pickle.load(file)


def show_predict_page():
    st.title("EduSustain")

    st.write("""### We need some information to predict the if the student is a dropout or graduate""")
    
    #values mapping
    marital_status = {2:"Married",1:"Single",4:"Divorced",3:"Widower",6:"Legally Seperated", 5:"Facto Union"}
    qualifications = {
        1:"Secondary Education—12th Year of Schooling or Equivalent",
        2:"Higher Education—bachelor's degree",
        3:"Higher Education—degree",
        4:"Higher Education—master's degree",
        5:"Higher Education—doctorate",
        6:"Frequency of Higher Education",
        7:"12th Year of Schooling—not completed",
        8:"11th Year of Schooling—not completed",
        9:"7th Year (Old)",
        10:"Other—11th Year of Schooling",
        11:"2nd year complementary high school course",
        12:"10th Year of Schooling",
        13:"General commerce course",
        14:"Basic Education 3rd Cycle (9th/10th/11th Year) or Equivalent",
        15:"Complementary High School Course",
        16:"Technical-professional course",
        17:"Complementary High School Course—not concluded",
        18:"7th year of schooling",
        19:"2nd cycle of the general high school course",
        20:"9th Year of Schooling—not completed",
        21:"8th year of schooling",
        22:"General Course of Administration and Commerce",
        23:"Supplementary Accounting and Administration",
        24:"Unknown",
        25:"Cannot read or write",
        26:"Can read without having a 4th year of schooling",
        27:"Basic education 1st cycle (4th/5th year) or equivalent",
        28:"Basic Education 2nd Cycle (6th/7th/8th Year) or equivalent",
        29:"Technological specialization course",
        30:"Higher education—degree (1st cycle)",
        31:"Specialized higher studies course",
        32:"Professional higher technical course",
        33:"Higher Education—master's degree (2nd cycle)",
        34:"Higher Education—doctorate (3rd cycle)"}
    nationalities = {         	1:"Portuguese",
            2:"German",
            3:"Spanish",
            4:"Italian",
            5:"Dutch",
            6:"English",
            7:"Lithuanian",
            8:"Angolan",
            9:"Cape Verdean",
            10:"Guinean",
            11:"Mozambican",
            12:"Santomean",
            13:"Turkish",
            14:"Brazilian",
            15:"Romanian",
            16:"Moldova (Republic of)",
            17:"Mexican",
            18:"Ukrainian",
            19:"Russian",
            20:"Cuban",
            21:"Colombian",

    }
    Nationalities = st.selectbox("Nationality",nationalities.values())
    Age = st.slider("Age at enrollement", 18, 30)
    Marital_status = st.selectbox("Marital Status",marital_status.values())
    previousqualifications = st.selectbox("Previous Qualifications", qualifications.values())
    mothersqualifications = st.selectbox("Mother's Qualifications", qualifications.values())
    fathersqualifications = st.selectbox("Father's Qualifications", qualifications.values())
    Enrolled1sem = st.slider("Enrolled units for the first semester", 0, 26, 1)
    units1_approved = st.slider("Approved units for the first semester", 0, Enrolled1sem, 1)
    Enrolled2sem = st.slider("Enrolled units for the second semester", 0, 23, 1)
    units2_approved = st.slider("Approved units for the second semester", 0, Enrolled2sem, 1)

    ok = st.button("Predict Class")
    for k,v in marital_status.items():
            if v.lower() == Marital_status.lower() :
                marital_status_b = k
                break
    for k,v in qualifications.items():
            if v.lower() == mothersqualifications.lower() :
                mothersqualifications_b = k
                break
    for k,v in qualifications.items():
            if v.lower() == fathersqualifications.lower() :
                fathersqualifications_b = k
                break
    for k,v in qualifications.items():
        if v.lower() == previousqualifications.lower() :
            previousqualifications_b = k
            break
    for k,v in nationalities.items():
            if v.lower() == Nationalities.lower() :
                nationalities_b = k
                break
    age_b = Age
    
    #gettings user input binary values
    if ok :
        X = [[marital_status_b,nationalities_b,previousqualifications_b,mothersqualifications_b,fathersqualifications_b,age_b,Enrolled1sem,units1_approved,Enrolled2sem,units2_approved]]
        Target = model.predict(X)
        if int(Target) == 0:
              Target_catagorical = "Dropout"
        elif int(Target) == 1 :
              Target_catagorical = "Graduate"
        Target_catagorical 
        st.subheader("The predicted class is "+Target_catagorical)
    
    
import streamlit as st

st.title("Title: Bio Data")
st.write("This is a sample web app.")

first_name = st.text_input("First Name")
last_name = st.text_input("Last Name")
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
age = st.number_input("Age", 0, 100, 30, 1)
dob = st.date_input("Your Birth Date")
marital_status = st.radio("Marital Status", ["Single", "Married", "Divorced", "Widowed"])
years_of_experience = st.slider("Years of Experience", 0, 50, 5)

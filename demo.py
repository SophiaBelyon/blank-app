# A simple streamlit app to collect bio data
#importing streamlit library
import streamlit as st

# Setting the title and a brief description of the app
st.title("Title: Bio Data")
st.write("This is a sample web app.")

# Creating input field for first name
first_name = st.text_input("First Name")
# Creating an input field for last name
last_name = st.text_input("Last Name")
# Creating select box to choose a gender
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
# creating a number input for age 
age = st.number_input("Age", 0, 100, 30, 1)
# Creating a date input field for date of birth
dob = st.date_input("Your Birth Date")
# Creating a radio button(an option button)for users to select their marital status 
marital_status = st.radio("Marital Status", ["Single", "Married", "Divorced", "Widowed"])
# Creating a slider to select years of experience 
years_of_experience = st.slider("Years of Experience", 0, 50, 5)

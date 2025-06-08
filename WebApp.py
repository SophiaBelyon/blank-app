#importing necessary libraraies
import pickle
import numpy as np
import streamlit as st
#loading the pre-trained model
model = pickle.load(open('model.pkl', 'rb'))
#setting the columns of the web app
col0, col1, col2, col3, col4, col5, col6 = st.columns(7)
#setting column 0 of the web app
with col0:
    st.write('')
    #setting column 1 of the web app
with col1:
    st.write('')
    #setting column 2 of the web app
with col2:
    st.write('') 
    #setting the title of the web app using markdown  
with col3:
    st.markdown("<h3 style='text-align: center; color: white;'>💲JANS SALARY PREDICTOR💲</h3>", unsafe_allow_html=True)
    #setting column 4 of the web app
with col4:
    st.write('')
with col5:
    st.write('')
with col6:
    st.write('')
# Creates  another row with three columns to center the subtitle
col7, col9 = st.columns(2)
with col7:
    st.write('')    
with col9:
    st.write('')
#Lists defining options for user input
gen_list = ["Female", "Male", "Other"]	
edu_list = ["Bachelor's", "Master's", "PhD"]
job_list = ["Director of Marketing", "Director of Operations", "Senior Data Scientist", "Senior Financial Analyst", "Senior Software Engineer"]
#Maps the job titles to numeric values(Corresponding indices for job titles)
job_idx = [0, 1, 10, 11, 20]
#Creates input fields for user data
gender = st.radio('Pick your gender👥', gen_list)# Radio Buttons to select gender
age = st.slider('Pick your age✍️', 21, 65)# Slider to select age btwn 21 and 55
education = st.selectbox('Pick your education level📚', edu_list)# Dropdown to select education level
job = st.selectbox('Pick your job title🥼', job_list)# Dropdown to select job title
experience = st.slider('Pick your years of experience🔢', 0.0, 25.0, 0.0, 0.5, "%1f")# Slider to select years of experience(from 0 to 25 years)with 0.5 year increments
# Creates a 5 column layout used to center the 'Predict Salary'button
col10, col11, col12, col13, col14 = st.columns(5)
with col10:
    st.write('')
with col11:
    st.write('')    
with col12:
    #This button triggers salary prediction
    predict_btn = st.button('Predict Salary')
with col13: 
    st.write('')
with col14:
    st.write('')

if(predict_btn):
    inp1 = int(age) # Converts age to integer
    # Converts years of experience to float
    inp2 = float(experience)
    # Maps the job title to its corresponding index value
    inp3 = int(job_idx[job_list.index(job)])
    # Maps the education to its corresponding index value
    inp4 = int(edu_list.index(education))
    # Maps the gender to its corresponding index value
    # (0 for Female, 1 for Male)
    inp5 = int(gen_list.index(gender))
    # Creates a list of inputs to be fed into the model for prediction
    X = [inp1, inp2, inp3, inp4, inp5]
    salary = model.predict([X]) # Predicts the salary using the model
    # Creates another row with three columns to display the predicted salary
    col15, col16, col17 = st.columns(3)
    with col15: #Fist column for spacing
        st.write('')    
    with col16: # Second column to display the predicted salary
        st.text(f"Estimated salary: ${int(salary[0])}") # Displays the predicted salary
    # Third column for spacing
    with col17:
        st.write('')


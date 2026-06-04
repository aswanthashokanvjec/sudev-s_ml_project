import streamlit as st
import pandas as pd
import pickle
with open('employee.pkl','rb') as f:
    model=pickle.load(f)
st.title(" Employee Performance Prediction")
experience = st.number_input("Experience Years", min_value=0)
workhours = st.number_input("Work Hours Per Week", min_value=0)
skill = st.number_input("Skill Score", min_value=0)
projects = st.number_input("Projects Handled", min_value=0)
training = st.number_input("Training Hours", min_value=0)
if st.button("Predict"):
    data = pd.DataFrame([[
        experience,
        workhours,
        skill,
        projects,
        training
        ]
    ])

    prediction = model.predict(data)
    st.subheader(f"Predicted Performance Score: {prediction[0]:.2f}")
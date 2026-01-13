import streamlit as st 
import numpy as np
import joblib

model = joblib.load("MOdel.pkl")

st.title("Titanic Survival Prediction.")
st.divider()

pclass = st.selectbox("Passenger Class (1=1st, 2=2nd, 3=3rd)",[1,2,3])
sex = st.selectbox("Gender",["Male","Female"])
age = st.number_input("Age",min_value=2, max_value=80, value=15)
sibsp = st.number_input("Number of sibling", min_value=0, max_value=10, value=0)
parch = st.number_input("Number of Parent", min_value=0, max_value=3, value=0)
Fare = st.number_input("Fare",min_value=0.0, max_value=6000.0, value=30.0)
embarked = st.selectbox("Port of Embarkation",["C","S","Q"])

sex_num = 1 if sex=="Male" else 0
embarked_mapping = {"S":0, "C":1, "Q":2}
embarked_num = embarked_mapping[embarked]


input_data = np.array([[pclass,sex_num,age,sibsp,parch,Fare, embarked_num]])

if st.button("Predict"):
    result = model.predict(input_data)
    if result[0]==1:
        st.success("Survived")
    else:
        st.error("Did not Survived")    
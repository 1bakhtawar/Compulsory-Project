# Project 9: Build a Python Website in 15 Minutes With Streamlit

import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="Student Data Generator", layout="wide")
st.title("Student CSV File Generator")

names = ["Ali","Hamza" , "Ayesha", "Hassan" ,"Sara" , "Rabab", "Alisha", "Tariq", "Bilal", "Zain" ,"Aneeq", "Laiba", "Maira", "Aalia"]

students =[]
for i in range(1,15):
    student = {
        "ID" : i,
        "Name" : random.choice(names),
        "Age" :random.randint(18,25),
        "Grade": random.choice(["A", "B" , "C" , "D" , "E", "F"]),
        "Marks": random.randint(40,100)
    }
    students.append(student)

df = pd.DataFrame(students)
st.subheader("Generator Students Data")
st.dataframe(df)

csv_file = df.to_csv(index=False).encode('utf-8')
st.download_button("Download CSV File" , csv_file, "students.csv" , "text/csv")
st.success("Students Record Generator Successfully!")
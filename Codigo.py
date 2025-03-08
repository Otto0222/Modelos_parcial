import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

#Load dataset
df = pd.read_csv('university_student_dashboard_data.csv')

#Inspect dataset
print(df.head())


# Sidebar Filters
st.sidebar.header("Filters")
selected_term = st.sidebar.selectbox("Select Term", df["Term"].unique())

# KPI Calculations
total_applications = df[df["Term"] == selected_term]["Applications"].sum()
total_admissions = df[df["Term"] == selected_term]["Admitted"].sum()
total_enrollments = df[df["Term"] == selected_term]["Enrolled"].sum()
retention_rate = df[df["Term"] == selected_term]["Retention Rate (%)"].mean()
satisfaction_score = df[df["Term"] == selected_term]["Student Satisfaction (%)"].mean()

# Dashboard Title
st.title("University Admissions & Student Satisfaction Dashboard")

# Display KPIs
st.metric("Total Applications", total_applications)
st.metric("Total Admissions", total_admissions)
st.metric("Total Enrollments", total_enrollments)
st.metric("Average Retention Rate", f"{retention_rate:.2f}%")
st.metric("Average Satisfaction Score", f"{satisfaction_score:.2f}/10")

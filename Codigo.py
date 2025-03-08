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
selected_year = st.sidebar.selectbox("Select Year", df["Year"].unique())
selected_term = st.sidebar.selectbox("Select Term", df["Term"].unique())

# Filter Data
df_filtered = df[(df["Year"] == selected_year) & (df["Term"] == selected_term)]

# KPI Calculations
total_applications = df_filtered["Applications"].sum()
total_admissions = df_filtered["Admitted"].sum()
total_enrollments = df_filtered["Enrolled"].sum()
retention_rate = df_filtered["Retention Rate (%)"].mean()
satisfaction_score = df_filtered["Student Satisfaction (%)"].mean()


# Dashboard Title
st.title("University Admissions & Student Satisfaction Dashboard")

# Display KPIs
st.metric("Total Applications", total_applications)
st.metric("Total Admissions", total_admissions)
st.metric("Total Enrollments", total_enrollments)
st.metric("Average Retention Rate", f"{retention_rate:.2f}%")
st.metric("Average Satisfaction Score", f"{satisfaction_score:.2f}/10")

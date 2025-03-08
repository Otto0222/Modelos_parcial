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
filtered_df = df[(df["Year"] == selected_year) & (df["Term"] == selected_term)]

# KPI Calculations
total_applications = filtered_df["Applications"].iloc[0]
total_admissions = filtered_df["Admitted"].iloc[0]
total_enrollments = filtered_df["Enrolled"].iloc[0]
retention_rate = filtered_df["Retention Rate (%)"].iloc[0]
satisfaction_score = filtered_df["Student Satisfaction (%)"].iloc[0]


# Dashboard Title
st.title("University Admissions & Student Satisfaction Dashboard")

# Display KPIs
st.metric("Total Applications", total_applications)
st.metric("Total Admissions", total_admissions)
st.metric("Total Enrollments", total_enrollments)
st.metric("Average Retention Rate", f"{retention_rate:.2f}%")
st.metric("Average Satisfaction Score", f"{satisfaction_score:.2f}/10")

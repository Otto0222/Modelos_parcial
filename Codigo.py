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

# Filtered Data
df_filtered = df[(df["Term"] == selected_term)

# KPI Calculations
total_applications = df_filtered["Applications"].sum()
total_admissions = df_filtered["Admissions"].sum()
total_enrollments = df_filtered["Enrollments"].sum()
retention_rate = df_filtered["Retention Rate"].mean()
satisfaction_score = df_filtered["Satisfaction Score"].mean()

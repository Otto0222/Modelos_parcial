import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

#Load dataset
df = pd.read_csv('university_student_dashboard_data.csv')

#Inspect dataset
print(df.head())


# Interface
# Sidebar Filters
st.sidebar.header("Filters")
selected_year = st.sidebar.selectbox("Select Year", df["Year"].unique())
selected_term = st.sidebar.selectbox("Select Term", df["Term"].unique())

# Dashboard Title
st.title("University Admissions & Student Satisfaction Dashboard")


# Total applications, admissions and enrollments per term
# Filter Data
filtered_df = df[(df["Year"] == selected_year) & (df["Term"] == selected_term)]

# Ensure the filtered data is not empty before calculations
if not filtered_df.empty:
    # KPI Calculations
    total_applications = filtered_df["Applications"].sum()
    total_admissions = filtered_df["Admitted"].sum()
    total_enrollments = filtered_df["Enrolled"].sum()

# Display Total applications, admissions, and enrollments per term
st.metric("Total Applications", total_applications)
st.metric("Total Admissions", total_admissions)
st.metric("Total Enrollments", total_enrollments)


# Retention rate trends over time
# Group the retention rates by years
df_retention_trend = df.groupby(["Year"])["Retention Rate (%)"].mean().reset_index()

# Plot the retention rate trends across the years 
fig_retention = px.line(df_retention_trend, x="Year", y="Retention Rate (%)", title="Retention Rate Trends")
st.plotly_chart(fig_retention)


# Student Satisfaction Score over the years
# Group the student satisfaction by years
df_satisfaction_trend = df.groupby(["Year"])["Student Satisfaction (%)"].mean().reset_index()

# Plot the retention rate trends across the years 
fig_satisfaction = px.line(df_satisfaction_trend, x="Year", y="Student Satisfaction (%)", title="Student Satisfaction Trends")
st.plotly_chart(fig_satisfaction)



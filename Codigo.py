import pandas as pd
import plotly.express as px
import streamlit as st


#Load dataset
df = pd.read_csv('university_student_dashboard_data.csv')

#Inspect dataset
print(df.head())



# Create Interface and headlines
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

# Text interpretation from results
st.write("### Interpretación (Retention rate)")
st.write("La tasa de retención se había mostrado inestable al inicio, teniendo subidas y bajadas entre el 2015 y el 2020. Sin embargo, a partir del 2020 ha estado en ascenso, lo que sugiere un mayor número de estudiantes satisfechos con el servicio brindado por la universidad.")



# Student Satisfaction Score over the years
# Group the student satisfaction by years
df_satisfaction_trend = df.groupby(["Year"])["Student Satisfaction (%)"].mean().reset_index()

# Plot the Satisfaction Score trends across the years 
fig_satisfaction = px.line(df_satisfaction_trend, x="Year", y="Student Satisfaction (%)", title="Student Satisfaction Trends")
st.plotly_chart(fig_satisfaction)

# Text interpretation from results
st.write("### Interpretación (Satisfaction Score)")
st.write("La satisfacción de los estudiantes con el servicio prestado por la universidad puede confirmarse con la gráfica de satisfacción. Esta se mantiene en ascenso a excepción por una caída en el 2020, que se pudo dar por factores externos.")
st.write("También se puede observar que ha habido un gran aumento en la satisfacción de los estudiantes en comparación con el año inicial, habiendo aumentado la satisfacción del 78% al 88% en menos de 10 años.")



# Enrollment Breakdown by Department
if not filtered_df.empty:
    department_enrollment = filtered_df[["Engineering Enrolled", "Business Enrolled", "Arts Enrolled", "Science Enrolled"]].sum()
    department_df = pd.DataFrame({"Department": department_enrollment.index, "Enrolled": department_enrollment.values})
    fig_enrollment = px.bar(department_df, x="Department", y="Enrolled", title="Enrollment by Department", color="Department")
    st.plotly_chart(fig_enrollment)



# Compare trends between departments, retention rates, and satisfaction levels
department_trends = df.melt(id_vars=["Year"], 
                             value_vars=["Engineering Enrolled", "Business Enrolled", "Arts Enrolled", "Science Enrolled"], 
                             var_name="Department", 
                             value_name="Enrollment")
department_trends["Department"] = department_trends["Department"].str.replace(" Enrolled", "")
fig_department_trends = px.line(department_trends, x="Year", y="Enrollment", color="Department", title="Enrollment Trends by Department")
st.plotly_chart(fig_department_trends)

# Text interpretation from results
st.write("### Interpretación (Trends by departments)")
st.write("El número de estudiantes matriculados varía a lo largo de los departamentos. Se observa una mayor demanda en los departamentos de ingeniería y negocios en comparación con los de arte y ciencias")



# Comparison between Spring vs Fall trends
# Group the enrolled data by terms and year
df_term_comparison = df.groupby(["Term", "Year"])["Enrolled"].sum().reset_index()

# Plot the enrolled students across Spring and Fall
fig_term_comparison = px.line(df_term_comparison, x="Year", y="Enrolled", color="Term", title="Spring vs Fall Enrollment Trends")
st.plotly_chart(fig_term_comparison)

# Text interpretation from results
st.write("### Interpretación (Spring vs Fall trends)")
st.write("La matrícula se mantiene constante en las temporadas de primavera y otoño. Esto indica que no hay ninguna preferencia por parte de los estudiantes a matricular en una temporada u otra.")





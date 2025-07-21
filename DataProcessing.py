import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("NYResturantClean.csv")

st.set_page_config(page_title="NYC Restaurant Dashboard", layout="wide")

# --- Sidebar Filters ---
st.sidebar.header("Filter the data")
borough = st.sidebar.selectbox("Select Borough", sorted(df['BORO'].dropna().unique()))
grade = st.sidebar.multiselect("Select Grade", df['GRADE'].dropna().unique(), default=df['GRADE'].dropna().unique())

# Create a list of boroughs with "All" at the top
boroughs = ['All'] + sorted(df['BORO'].dropna().unique().tolist())
borough = st.sidebar.selectbox("Select Borough", boroughs)

# Multiselect for grades
grade = st.sidebar.multiselect(
    "Select Grade", 
    sorted(df['GRADE'].dropna().unique()), 
    default=sorted(df['GRADE'].dropna().unique())
)

# --- Apply Filters ---
# Borough filter
if borough == 'All':
    filtered_df = df.copy()
else:
    filtered_df = df[df['BORO'] == borough]

# Grade filter (applied after borough)
filtered_df = filtered_df[filtered_df['GRADE'].isin(grade)]

# --- Dashboard Header ---
st.title("NYC Restaurant Inspection Dashboard")
st.markdown("Explore health inspection data for restaurants across New York City.")

# --- Metric Summary ---
st.metric("Restaurants Shown", value=len(filtered_df))

# --- Cuisine Distribution Chart ---
st.subheader("Top 10 Cuisines")
top_cuisines = filtered_df['CUISINE_DESCRIPTION'].value_counts().head(10)
fig1 = px.bar(top_cuisines, title="Top 10 Cuisines in Selected Borough", labels={'index':'Cuisine', 'value':'Count'})
st.plotly_chart(fig1)

# --- Grade Distribution Chart ---
st.subheader("Top 10 Cuisines")
top_cuisines = filtered_df['GRADE'].value_counts().head(10)
fig4 = px.bar(top_cuisines, title="Grade Distribution", labels={'index':'Grade', 'value':'Count'})
st.plotly_chart(fig4)

# --- Grade Pie Chart ---
st.subheader("Grade Distribution")
fig2 = px.pie(filtered_df, names='GRADE', title='Distribution of Grades')
st.plotly_chart(fig2)

# --- Inspection Score Histogram ---
st.subheader("Inspection Score Distribution")
fig3 = px.histogram(filtered_df, x='SCORE', nbins=20, title="Histogram of Inspection Scores")
st.plotly_chart(fig3)

critical_df = df[df['CRITICAL_FLAG'] == 'Critical']

fig = px.scatter_mapbox(
    critical_df,
    lat="Latitude",
    lon="Longitude",
    hover_name="DBA",  # restaurant name
    hover_data=["BORO"],
    zoom=9.5,
    height=600
)

fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

st.subheader("Interactive Map of Critical Violations")
st.plotly_chart(fig)

# --- Data Table ---
st.subheader("Filtered Data Table")
st.dataframe(filtered_df)
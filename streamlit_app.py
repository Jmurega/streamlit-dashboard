import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Sales Dashboard")

data = {
    "Month": ["Jan","Feb","Mar","Apr","May","Jun"],
    "Sales": [15000,18000,21000,19000,22000,25000],
    "Category": ["Electronics","Furniture","Electronics","Furniture","Electronics","Furniture"]
}

df = pd.DataFrame(data)

st.subheader("Sales Data")
st.dataframe(df)

fig = px.line(df, x="Month", y="Sales", title="Monthly Sales Trend")
st.plotly_chart(fig)

fig2 = px.bar(df, x="Category", y="Sales", color="Category", title="Sales by Category")
st.plotly_chart(fig2)

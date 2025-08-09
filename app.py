import streamlit as st
import pandas as pd
import plotly.express as px

st.title("My first Streamlit app")

df = pd.DataFrame({
    "City": ["Tokyo", "Paris", "New York", "Berlin"],
    "Population": [37, 11, 19, 3]
})

fig = px.bar(df, x="City", y="Population", title="Population by city")
st.plotly_chart(fig)
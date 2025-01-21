import pandas as pd
import streamlit as st
import plotly.express as px
vehicles = pd.read_csv('vehicles_us.csv') # Load the vehicles DataFrame.

# Streamlit app strucutre
st.title("Vehicle Data Dashboard")
st.header("Overview")

# Display the dataset
if st.checkbox("Show raw data"):
    st.write(vehicles)

# Add Histogram for price distribution by vehicle type
st.header("Price Distribution by Vehicle Type")
fig = px.histogram(vehicles, x="price", color="type", nbins=50, title="Price Distribution by Vehicle Type")
st.plotly_chart(fig)

# Add interactivity
st.header("Filter by Max Price")
max_price = st.slider("Select the maximum price", 0, 100000, 50000)
filtered_data = vehicles[vehicles["price"] <= max_price]

# Let users select column to visualize
column = st.selectbox('Choose a column to visualize', vehicles.columns)
st.plotly_chart(px.histogram(vehicles, x=column))

# Scatterplot
st.header("Price vs. Odometer")
scatter_fig = px.scatter(
    filtered_data,
    x="odometer",
    y="price",
    color="type",
    title=f"Price vs Odometer (Max Price: ${max_price})"
)
st.plotly_chart(scatter_fig)
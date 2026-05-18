import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("products.csv")

# Page title
st.title("FATMEY Sales Dashboard")

st.subheader("Products Dataset")
st.dataframe(df)

# General statistics
st.subheader("General Statistics")

total_products = len(df)
total_stock = df["stock"].sum()
out_of_stock = len(df[df["stock"] == 0])

st.write(f"Total products: {total_products}")
st.write(f"Total stock units: {total_stock}")
st.write(f"Out of stock products: {out_of_stock}")

# Category chart
st.subheader("Products by Category")

category_counts = df["category"].value_counts()

fig, ax = plt.subplots()

category_counts.plot(kind="bar", ax=ax)

plt.title("Products by Category")

st.pyplot(fig)
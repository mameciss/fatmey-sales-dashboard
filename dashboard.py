import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="FATMEY Dashboard",
    layout="wide"
)

# FATMEY branding

st.image(
    "https://fatmeyshop.com/cdn/shop/files/logo.png",
    width=180
)

st.title("FATMEY Sales Dashboard")

st.markdown("""
### Beauty & Cosmetics Analytics Platform

Bienvenue sur le dashboard analytique de la marque FATMEY.

Ce dashboard permet de :
- suivre les stocks
- analyser les catégories
- visualiser les produits
- surveiller les performances commerciales

🌐 Site officiel :
- https://fatmeyshop.com
- https://fatmey.com
""")

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
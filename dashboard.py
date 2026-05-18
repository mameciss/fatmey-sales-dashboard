import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="FATMEY Dashboard",
    layout="wide",
    page_icon="✨"
)

st.sidebar.title("✨ FATMEY")
st.sidebar.markdown("### CEO Dashboard")

st.sidebar.info("""
FATMEY Analytics Platform

Beauty & Cosmetics 
""")

page = st.sidebar.radio(
    "Navigation",
    [
        "Overview",
        "Products",
        "Sales Analytics"
    ]
)

if page == "Overview":

    st.markdown("## Business Overview")

    st.metric("Revenue", "8,230,000 FG")
    st.metric("Orders", "16")
    st.metric("Units Sold", "48")


elif page == "Products":

    st.markdown("## Products Dataset")

   st.dataframe(df)

    st.markdown("## Stock Alerts")

    low_stock = df[df["stock"] <= 10]

    st.dataframe(low_stock)


elif page == "Sales Analytics":

    st.markdown("## Sales Analytics")

    st.markdown("### Revenue by Category")

    revenue_by_category = {
        "Haircare": 5350000,
        "Skincare": 1450000,
        "Makeup": 900000,
        "Beardcare": 530000
    }

    fig, ax = plt.subplots()

    ax.bar(
        revenue_by_category.keys(),
        revenue_by_category.values()
    )

    st.pyplot(fig)
st.markdown("""
# ✨ FATMEY Sales Dashboard

### Beauty & Cosmetics Analytics Platform

Welcome to the premium analytics dashboard for FATMEY.
""")



st.markdown("""
### Beauty & Cosmetics Analytics Platform

Bienvenue sur le dashboard analytique de la marque FATMEY en GUINÉE.

Ce dashboard permet de :
- suivre les stocks
- analyser les catégories
- visualiser les produits
- surveiller les performances commerciales

🌐 Sites officiel :
- https://fatmeyshop.com
- https://fatmey.com
""")

# Load data
df = pd.read_csv("products.csv")
orders = pd.read_csv("orders_simulated.csv")
orders["date"] = pd.to_datetime(orders["date"])

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

total_revenue = orders["revenue"].sum()
total_orders = len(orders)
total_units_sold = orders["quantity"].sum()


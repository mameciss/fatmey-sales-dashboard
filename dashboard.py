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

Beauty & Cosmetics Intelligence
""")

page = st.sidebar.radio(
    "Navigation",
    [
        "Overview",
        "Products",
        "Sales Analytics"
    ]
)

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
st.markdown("## Business Overview")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Revenue",
    f"{total_revenue:,} FG",
    "+12%"
)

col2.metric(
    "Orders",
    total_orders,
    "+8%"
)

col3.metric(
    "Units Sold",
    total_units_sold,
    "+15%"
)

total_revenue = orders["revenue"].sum()
total_orders = len(orders)
total_units_sold = orders["quantity"].sum()

col1, col2, col3 = st.columns(3)

col1.metric("Simulated Revenue", f"{total_revenue:,} FG")
col2.metric("Simulated Orders", total_orders)
col3.metric("Units Sold", total_units_sold)

st.subheader("Revenue by Category")

revenue_by_category = orders.groupby("category")["revenue"].sum().sort_values(ascending=False)

fig2, ax2 = plt.subplots()
revenue_by_category.plot(kind="bar", ax=ax2)
plt.title("Simulated Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue (FG)")
st.pyplot(fig2)

st.subheader("Top Selling Products")

top_products = orders.groupby("product")["quantity"].sum().sort_values(ascending=False).head(5)

st.dataframe(top_products)

st.subheader("Sales by Channel")

channel_sales = orders.groupby("channel")["revenue"].sum().sort_values(ascending=False)

fig3, ax3 = plt.subplots()
channel_sales.plot(kind="bar", ax=ax3)
plt.title("Simulated Revenue by Sales Channel")
plt.xlabel("Channel")
plt.ylabel("Revenue (FG)")
st.pyplot(fig3)
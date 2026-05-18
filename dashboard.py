import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="FATMEY Dashboard", layout="wide", page_icon="✨")

df = pd.read_csv("products.csv")
orders = pd.read_csv("orders_simulated.csv")
orders["date"] = pd.to_datetime(orders["date"])

total_revenue = orders["revenue"].sum()
total_orders = len(orders)
total_units_sold = orders["quantity"].sum()

st.sidebar.title("✨ FATMEY")
st.sidebar.markdown("### CEO Dashboard")
st.sidebar.info("FATMEY Analytics Platform\n\nBeauty & Cosmetics")

page = st.sidebar.radio("Navigation", ["Accueil", "Overview", "Products", "Sales Analytics"])

if page == "Accueil":
    st.markdown("# ✨ FATMEY")
    st.markdown("## Beauty & Cosmetics Analytics Platform")
    st.write("Bienvenue sur le dashboard analytique simulé de la marque FATMEY en Guinée.")

    st.markdown("""
    Ce tableau de bord permet de :
    - suivre les stocks
    - analyser les catégories
    - visualiser les produits
    - surveiller les performances commerciales
    - simuler les ventes par canal

    🌐 Sites officiels :
    - https://fatmeyshop.com
    - https://fatmey.com
    """)

elif page == "Overview":


    st.markdown("# ✨ FATMEY Sales Dashboard")
    st.markdown("### Beauty & Cosmetics Analytics Platform")
    st.write("Bienvenue sur le dashboard analytique simulé de FATMEY.")

    col1, col2, col3 = st.columns(3)
    col1.metric("Revenue", f"{total_revenue:,} FG", "+12%")
    col2.metric("Orders", total_orders, "+8%")
    col3.metric("Units Sold", total_units_sold, "+15%")

elif page == "Products":
    st.markdown("## Products Dataset")
    st.dataframe(df)

    st.markdown("## Stock Alerts")
    low_stock = df[df["stock"] <= 10]
    st.dataframe(low_stock)

elif page == "Sales Analytics":

    st.markdown("## Sales Analytics")

    selected_channel = st.selectbox(
        "Select Sales Channel",
        orders["channel"].unique()
    )

    filtered_orders = orders[
        orders["channel"] == selected_channel
    ]

    st.markdown("### Revenue by Category")

    revenue_by_category = filtered_orders.groupby(
        "category"
    )["revenue"].sum().sort_values(ascending=False)

    fig, ax = plt.subplots()

    revenue_by_category.plot(
        kind="bar",
        ax=ax
    )

    ax.set_title("Simulated Revenue by Category")
    ax.set_xlabel("Category")
    ax.set_ylabel("Revenue (FG)")

    st.pyplot(fig)

    st.markdown("### Top Selling Products")

    top_products = filtered_orders.groupby(
        "product"
    )["quantity"].sum().sort_values(
        ascending=False
    ).head(5)

    st.dataframe(top_products)

    st.markdown("### Sales by Channel")

    channel_sales = orders.groupby(
        "channel"
    )["revenue"].sum().sort_values(
        ascending=False
    )

    fig2, ax2 = plt.subplots()

    channel_sales.plot(
        kind="bar",
        ax=ax2
    )

    ax2.set_title("Simulated Revenue by Sales Channel")
    ax2.set_xlabel("Channel")
    ax2.set_ylabel("Revenue (FG)")

    st.pyplot(fig2)
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("ggplot")

st.set_page_config(
    page_title="FATMEY Dashboard",
    layout="wide",
    page_icon="✨"
)

st.markdown("""
<style>

/* Global */
.main {
    background-color: #F8F6F2;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #111827;
}

[data-testid="stSidebar"] * {
    color: white;
}

/* Titles */
h1 {
    color: #111827;
    font-weight: 800;
}

h2, h3 {
    color: #1F2937;
}

/* Metrics */
[data-testid="metric-container"] {
    background-color: white;
    border: 1px solid #E5E7EB;
    padding: 20px;
    border-radius: 14px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.04);
}

/* Buttons */
.stButton>button {
    background-color: #C19A6B;
    color: white;
    border-radius: 10px;
    border: none;
    padding: 0.5rem 1rem;
}

/* Tables */
[data-testid="stDataFrame"] {
    background-color: white;
    border-radius: 10px;
}

/* Alerts */
.stAlert {
    border-radius: 12px;
}

</style>
""", unsafe_allow_html=True)
products = pd.read_csv("products.csv")
orders = pd.read_csv("orders_simulated.csv")
orders["date"] = pd.to_datetime(orders["date"])

total_revenue = orders["revenue"].sum()
total_orders = len(orders)
total_units_sold = orders["quantity"].sum()
average_order_value = total_revenue / total_orders

st.sidebar.title("✨ FATMEY")
st.sidebar.markdown("### CEO Dashboard")
st.sidebar.info("Données simulées pour portfolio tech/business.")

page = st.sidebar.radio(
    "Navigation",
    ["Accueil", "Overview", "Products", "Sales Analytics", "CEO Insights"]
)

if page == "Accueil":
    st.markdown("# ✨ FATMEY Analytics Dashboard")
    st.markdown("## Beauty & Cosmetics Business Intelligence")

    st.write(
        "Bienvenue sur le dashboard analytique simulé de FATMEY. "
        "Ce projet présente une solution de suivi des stocks, ventes et performances commerciales."
    )

    st.warning("Les données utilisées sont simulées. Aucune donnée client réelle n’est utilisée.")

    st.markdown("""
### Objectifs du dashboard
- Suivre les stocks
- Identifier les produits en rupture
- Analyser les ventes par catégorie
- Comparer les canaux de vente
- Visualiser les produits les plus performants

### Sites officiels
- https://fatmeyshop.com
- https://fatmey.com
""")

elif page == "Overview":
    st.markdown("# Business Overview")
st.markdown("""
Analyse globale des ventes, commandes et performances commerciales simulées de FATMEY.
""")
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Revenue", f"{total_revenue:,} FG", "+12%")
    col2.metric("Orders", total_orders, "+8%")
    col3.metric("Units Sold", total_units_sold, "+15%")
    col4.metric("Avg Order Value", f"{average_order_value:,.0f} FG", "+5%")

    st.markdown("## Sales Over Time")

    sales_over_time = orders.groupby("date")["revenue"].sum()

 fig, ax = plt.subplots(figsize=(12, 5))
fig.patch.set_facecolor("#F8F6F2")
ax.set_facecolor("white")

    sales_over_time.plot(
    kind="line",
    marker="o",
    linewidth=3,
    markersize=8,
    ax=ax,
    color="#C19A6B"
)

    ax.set_title("Simulated Revenue Over Time")
    ax.set_xlabel("Date")
    ax.set_ylabel("Revenue (FG)")
    st.pyplot(fig)

elif page == "Products":
    st.markdown("# Products & Inventory")

    st.dataframe(products, use_container_width=True)

    st.markdown("## Inventory Summary")

    total_products = len(products)
    total_stock = products["stock"].sum()
    out_of_stock = len(products[products["stock"] == 0])
    inventory_value = (products["price"] * products["stock"]).sum()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Products", total_products)
    col2.metric("Stock Units", total_stock)
    col3.metric("Out of Stock", out_of_stock)
    col4.metric("Inventory Value", f"{inventory_value:,} FG")

    st.markdown("## Stock Alerts")

    low_stock = products[(products["stock"] > 0) & (products["stock"] <= 10)]
    no_stock = products[products["stock"] == 0]

    st.markdown("### Low Stock")
    st.dataframe(low_stock, use_container_width=True)

    st.markdown("### Out of Stock")
    st.dataframe(no_stock, use_container_width=True)

elif page == "Sales Analytics":
    st.markdown("# Sales Analytics")

st.markdown("""
Visualisation analytique des revenus, catégories et canaux de vente.
""")

    st.sidebar.markdown("## Filters")

    selected_channel = st.sidebar.multiselect(
        "Sales Channel",
        options=orders["channel"].unique(),
        default=orders["channel"].unique()
    )

    selected_category = st.sidebar.multiselect(
        "Category",
        options=orders["category"].unique(),
        default=orders["category"].unique()
    )

    date_range = st.sidebar.date_input(
        "Date Range",
        value=(
            orders["date"].min(),
            orders["date"].max()
        )
    )

    if len(date_range) == 2:
        start_date = pd.to_datetime(date_range[0])
        end_date = pd.to_datetime(date_range[1])
    else:
        start_date = orders["date"].min()
        end_date = orders["date"].max()

    filtered_orders = orders[
        (orders["channel"].isin(selected_channel)) &
        (orders["category"].isin(selected_category)) &
        (orders["date"] >= start_date) &
        (orders["date"] <= end_date)
    ]

    filtered_revenue = filtered_orders["revenue"].sum()
    filtered_orders_count = len(filtered_orders)
    filtered_units = filtered_orders["quantity"].sum()

    col1, col2, col3 = st.columns(3)
    col1.metric("Filtered Revenue", f"{filtered_revenue:,} FG")
    col2.metric("Filtered Orders", filtered_orders_count)
    col3.metric("Filtered Units Sold", filtered_units)

    st.markdown("## Revenue by Category")

    revenue_by_category = filtered_orders.groupby("category")["revenue"].sum().sort_values(ascending=False)

    if revenue_by_category.empty:
        st.warning("No data available for selected filters.")
    else:

fig, ax = plt.subplots(figsize=(10, 5))
fig.patch.set_facecolor("#F8F6F2")
ax.set_facecolor("white")

        revenue_by_category.plot(kind="bar", ax=ax, color="#F4A261")
        ax.set_title("Revenue by Category")
        ax.set_xlabel("Category")
        ax.set_ylabel("Revenue (FG)")
        st.pyplot(fig)

    st.markdown("## Sales by Channel")

    sales_by_channel = filtered_orders.groupby("channel")["revenue"].sum().sort_values(ascending=False)

    if sales_by_channel.empty:
        st.warning("No channel data available.")
    else:
        fig2, ax2 = plt.subplots(figsize=(8, 4))
        sales_by_channel.plot(kind="bar", ax=ax2, color="#2A9D8F")
        ax2.set_title("Revenue by Sales Channel")
        ax2.set_xlabel("Channel")
        ax2.set_ylabel("Revenue (FG)")
        st.pyplot(fig2)

    st.markdown("## Top Selling Products")

    top_products = filtered_orders.groupby("product")["quantity"].sum().sort_values(ascending=False).head(5)

    if top_products.empty:
        st.warning("No product data available.")
    else:
        st.dataframe(top_products, use_container_width=True)

elif page == "CEO Insights":
    st.markdown("# CEO Insights")
st.info("Résumé exécutif des performances commerciales et recommandations stratégiques.")
    best_channel = orders.groupby("channel")["revenue"].sum().idxmax()
    best_category = orders.groupby("category")["revenue"].sum().idxmax()
    best_product = orders.groupby("product")["quantity"].sum().idxmax()

    st.success(f"Best sales channel: {best_channel}")
    st.success(f"Top revenue category: {best_category}")
    st.success(f"Best-selling product: {best_product}")

    st.markdown("""
### Recommendations
- Restock products with low inventory.
- Prioritize marketing campaigns on the strongest sales channel.
- Promote the best-performing category more aggressively.
- Monitor out-of-stock products weekly.
""")

st.markdown("---")
st.caption(
    "FATMEY Analytics Dashboard — Simulated portfolio project built with Python, Pandas, Matplotlib and Streamlit."
)
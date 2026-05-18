import pandas as pd

# Load dataset
df = pd.read_csv("products.csv")

# Display dataset
print("\n===== FATMEY SALES DASHBOARD =====\n")

print("Products dataset:\n")
print(df)

# General statistics
print("\n===== GENERAL STATISTICS =====\n")

total_products = len(df)
total_stock = df["stock"].sum()
out_of_stock = len(df[df["status"] == "Out of Stock"])

print(f"Total products: {total_products}")
print(f"Total stock units: {total_stock}")
print(f"Out of stock products: {out_of_stock}")

# Average price
average_price = df["price"].mean()

print(f"Average product price: {average_price:.0f} FG")

# Products by category
print("\n===== PRODUCTS BY CATEGORY =====\n")

category_counts = df["category"].value_counts()

print(category_counts)

# Most expensive products
print("\n===== TOP EXPENSIVE PRODUCTS =====\n")

top_products = df.sort_values(by="price", ascending=False)

# Stock alerts
print("\n===== STOCK ALERTS =====\n")

low_stock = df[(df["stock"] > 0) & (df["stock"] <= 10)]
out_stock = df[df["stock"] == 0]

print("Low stock products:")
print(low_stock[["product", "stock"]])

print("\nOut of stock products:")
print(out_stock[["product", "stock"]])

# Potential inventory value
print("\n===== INVENTORY VALUE =====\n")

df["inventory_value"] = df["price"] * df["stock"]
total_inventory_value = df["inventory_value"].sum()

print(f"Total inventory value: {total_inventory_value:,} FG")

print(top_products[["product", "price"]].head(5))
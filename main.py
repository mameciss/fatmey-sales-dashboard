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

print(top_products[["product", "price"]].head(5))
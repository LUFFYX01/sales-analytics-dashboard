# a general understanding of prjoect how it will work 
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/raw/sales.csv")

# ------------------------------------
# Basic Data Understanding
# ------------------------------------


print("FIRST 5 ROWS:\n")
print(df.head())

print("\nSHAPE:\n")
print(df.shape)

print("\nCOLUMNS:\n")
print(df.columns)

print("\nINFO:\n")
print(df.info())

print("\nMISSING VALUES:\n")
print(df.isnull().sum())

print("\nDUPLICATES:\n")
print(df.duplicated().sum())

# --------------------------------------
# Data Cleaning
# --------------------------------------

# Drop Postal code column 
df = df.drop(columns=['Postal Code'])

# Convert OrderDate to Date-time
df['Order Date'] = pd.to_datetime(df['Order Date'],dayfirst = True)

# Create Month and Year Column
df['month'] = df['Order Date'].dt.month
df['year'] = df['Order Date'].dt.year

# --------------------------------------
# Monthly Revenue Analysis
# --------------------------------------
monthly_sales = df.groupby('month')['Sales'].sum()
print("\nMONTHLY SALES : \n")
print(monthly_sales)

highest_sales_month = monthly_sales.idxmax()
highest_sales_value = monthly_sales.max()

print("\nHIGHEST SALES MONTH:\n")
print(f"Month: {highest_sales_month}")
print(f"Sales: {highest_sales_value}")

# ------------------------------
# visualisation of monthly sales
# ------------------------------

# monthly_sales.plot(kind = 'line',marker ='o')

# plt.title("Monthly Sales Trend")
# plt.xlabel("Month")
# plt.ylabel("Sales")

# plt.savefig("outputs/charts/monthly_sales.png")

# plt.show()

# --------------------------------------
# Top Selling Products
# --------------------------------------

top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending = False).head(10)

print("\n TOP PRODUCTS : \n")
print(top_products)

best_product = top_products.idxmax()

print("\nBEST PRODUCT:\n")
print(best_product)

# ------------------------
# Top Products Bar Chart
# ------------------------

# top_products.plot(kind = 'bar')

# plt.title("Top Products Chart")
# plt.xlabel("Products")
# plt.ylabel("Sales")

# plt.yticks(rotation = 45)

# plt.savefig("outputs/charts/top_products.png")

# plt.show()

# -------------------------------------
# Region wise Sales
# -------------------------------------
region_sales = df.groupby('Region')['Sales'].sum()

print("\nREGION SALES :\n")
print(region_sales)

best_region = region_sales.idxmax()

print("\nBEST REGION:\n")
print(best_region)

# -------------------------------
# Region-wise Pie Chart
# -------------------------------

# region_sales.plot(kind = 'pie', autopct = '%1.1f%%')

# plt.title("Region-wise Sales")
# plt.ylabel("")

# plt.savefig("outputs/charts/region_sales.png")

# plt.show()



# ------------------------------------
# Category-wise sales
# ------------------------------------
category_sales = df.groupby('Category')['Sales'].sum()

print("\nSALES BY CATEGORY :\n")
print(category_sales)

best_category = category_sales.idxmax()

print("\nBEST CATEGORY:\n")
print(best_category)


# --------------------------------------
# Verify Changes
# --------------------------------------

print("\n UPDATED DATA:\n")
print(df[['Order Date','month','year']].head())

print("\n------ BUSINESS INSIGHTS ------")

print(f"Highest sales were recorded in month {highest_sales_month}.")

print(f"The best performing region is {best_region}.")

print(f"The top-selling product is {best_product}.")

print(f"The category with highest sales is {best_category}.")
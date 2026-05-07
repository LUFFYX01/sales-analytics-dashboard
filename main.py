import pandas as pd

from src.data_cleaning import clean_data

from src.analysis import (
    monthly_sales_analysis,
    top_products_analysis,
    region_sales_analysis,
    category_sales_analysis
)

from src.visualization import (
    plot_monthly_sales,
    plot_top_products,
    plot_region_sales
)

from src.analysis import (
    monthly_sales_analysis,
    top_products_analysis,
    region_sales_analysis,
    category_sales_analysis,
    sales_statistics
)

# Load Dataset
df = pd.read_csv("data/raw/sales.csv")

# Clean Dataset
df = clean_data(df)

# Processed Data
df.to_csv(
    "data/processed/clean_sales.csv",
    index=False
)

# Perform Analysis
monthly_sales = monthly_sales_analysis(df)

top_products = top_products_analysis(df)

region_sales = region_sales_analysis(df)

category_sales = category_sales_analysis(df)

sales_stats = sales_statistics(df)

# Generate Visualizations
plot_monthly_sales(monthly_sales)

plot_top_products(top_products)

plot_region_sales(region_sales)

# Sales Insights

print("\n------ SALES STATISTICS ------")

for key, value in sales_stats.items():

    print(f"{key}: {value}")

# Business Insights
print("\n------ BUSINESS INSIGHTS ------")

print(
    f"Highest sales were recorded in month "
    f"{monthly_sales.idxmax()}."
)

print(
    f"The best performing region is "
    f"{region_sales.idxmax()}."
)

print(
    f"The top-selling product is "
    f"{top_products.idxmax()}."
)

print(
    f"The category with highest sales is "
    f"{category_sales.idxmax()}."
)
# 📊 Sales Analytics Dashboard

## 🔍 Overview

This project performs sales data analysis on a retail Superstore dataset using Python.  
The goal of the project is to clean and analyze sales data to identify:
- Monthly sales trends
- Top-selling products
- Region-wise sales performance
- Category-wise business insights

The project includes:
- Data Cleaning
- Exploratory Data Analysis (EDA)
- Statistical Analysis
- Data Visualization

---

# 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib

---

# 📂 Dataset Information

- Total Records: 9,800
- Total Columns: 18
- Dataset Type: Retail Superstore Sales Data

### Key Features Used
- Order Date
- Region
- Category
- Sub-Category
- Product Name
- Sales
- State
- Segment

---

# 📂 Project Structure

```bash
sales-analysis/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── outputs/
│   └── charts/
│
├── src/
│   ├── data_cleaning.py
│   ├── analysis.py
│   └── visualization.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

# 🧹 Data Preprocessing

The following preprocessing steps were performed:

- Removed unnecessary columns
- Converted `Order Date` to datetime format
- Created Month and Year features
- Generated processed dataset
- Checked missing values and duplicates

---

# 📊 Analysis Performed

## 1️⃣ Monthly Sales Analysis
- Identified monthly sales trends
- Determined highest-performing sales month

## 2️⃣ Top-Selling Products
- Identified top 10 products by revenue
- Analyzed product-wise sales contribution

## 3️⃣ Region-wise Sales Analysis
- Compared sales performance across regions
- Identified best-performing region

## 4️⃣ Category-wise Sales Analysis
- Compared category sales performance
- Identified highest revenue-generating category

## 5️⃣ Statistical Analysis (NumPy)
Performed:
- Mean Sales
- Median Sales
- Maximum Sales
- Minimum Sales
- Standard Deviation

---

# 📈 Visualizations

- Monthly Sales Trend Line Chart
- Top Products Bar Chart
- Region-wise Sales Distribution Pie Chart

---

# 💡 Key Insights

- Technology category generated the highest sales
- Sales performance varied significantly across regions
- A small number of products contributed major revenue share
- Certain months showed noticeably higher sales trends

---

# ▶️ How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python main.py
```

---

# 📂 Output Generated

The project generates:
- Cleaned dataset
- Business insights
- Statistical analysis
- Visualization charts

Charts are saved inside:

```bash
outputs/charts/
```

---

# 🚀 Future Improvements

- Power BI Dashboard Integration
- Streamlit Dashboard
- SQL Database Integration
- Sales Forecasting
- KPI Dashboard

---

# 👨‍💻 Author

Prateek - (https://linkedin.com/in/prateek-gupta-a42247293)

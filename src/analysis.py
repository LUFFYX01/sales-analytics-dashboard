import numpy as np

def monthly_sales_analysis(df):

    return df.groupby('Month')['Sales'].sum()


def top_products_analysis(df):

    return (
        df.groupby('Product Name')['Sales']
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

def sales_statistics(df):

    sales_data = df['Sales'].values

    stats = {
        'Average Sales': np.mean(sales_data),
        'Median Sales': np.median(sales_data),
        'Maximum Sales': np.max(sales_data),
        'Minimum Sales': np.min(sales_data),
        'Standard Deviation': np.std(sales_data)
    }

    return stats


def region_sales_analysis(df):

    return df.groupby('Region')['Sales'].sum()


def category_sales_analysis(df):

    return df.groupby('Category')['Sales'].sum()
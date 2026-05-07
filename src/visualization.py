import matplotlib.pyplot as plt


def plot_monthly_sales(monthly_sales):

    monthly_sales.plot(
        kind='line',
        marker='o'
    )

    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Sales")

    plt.savefig(
        "outputs/charts/monthly_sales.png"
    )

    plt.show()


def plot_top_products(top_products):

    top_products.plot(kind='bar')

    plt.title("Top Selling Products")
    plt.xlabel("Products")
    plt.ylabel("Sales")

    plt.xticks(rotation=45)

    plt.savefig(
        "outputs/charts/top_products.png"
    )

    plt.show()


def plot_region_sales(region_sales):

    region_sales.plot(
        kind='pie',
        autopct='%1.1f%%'
    )

    plt.title("Region-wise Sales")
    plt.ylabel("")

    plt.savefig(
        "outputs/charts/region_sales.png"
    )

    plt.show()
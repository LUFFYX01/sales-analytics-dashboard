import pandas as pd


def clean_data(df):

    # Remove unnecessary column
    df = df.drop(columns=['Postal Code'])

    # Convert date column
    df['Order Date'] = pd.to_datetime(
        df['Order Date'],
        dayfirst=True
    )

    # Feature engineering
    df['Month'] = df['Order Date'].dt.month
    df['Year'] = df['Order Date'].dt.year

    return df
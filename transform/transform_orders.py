import pandas as pd

def transform_orders(df):
    df=df.copy()
    n=df.duplicated().sum()
    if n>0:
        df=df.drop_duplicates()
    df["order_amount"]=pd.to_numeric(df["order_amount"],errors='coerce')
    df["quantity"]=pd.to_numeric(df["quantity"],errors='coerce')
    df["order_date"]=pd.to_datetime(df["order_date"],errors='coerce')

    return df

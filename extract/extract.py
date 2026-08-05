import pandas as pd

def extract_orders(path):
    return pd.read_csv(path)


def extract_customers(path):
    return pd.read_csv(path)


def extract_support_ticket(path):
    return pd.read_csv(path)
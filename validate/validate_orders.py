import pandas as pd

def validate_orders(df):

    valid=df.copy()
    invalid=pd.DataFrame()

    negative_amount=valid[valid["order_amount"]<0]
    invalid["validation_error"]="order_amount is negative"
    invalid=pd.concat([negative_amount, invalid])

    negative_quantity=valid[valid["quantity"]<0]
    invalid["quantity_validation_error"]="quantity is negative"
    invalid=pd.concat([invalid, negative_quantity])

    null_date=valid[valid["order_date"].isna()]
    invalid["date_validation_error"]="order_date is null"
    invalid=pd.concat([invalid, null_date])

    valid=df[(
        df["order_amount"]>=0) &
        (df["quantity"]>=0) &
        (df["order_date"].notna()
    )]

    return valid, invalid
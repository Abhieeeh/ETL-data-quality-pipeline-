import pandas as pd
import logging
logger=logging.getLogger("__name__")

def validate_orders(df):
    logger.info("order data validation started")

    df=df.copy()


    df["validation_error"]=""

    # Negative order_amount
    df.loc[df["order_amount"]<0, "validation_error"]+="order_amount is negative;"

    # Negative quantity
    df.loc[df["quantity"]<0, "validation_error"]+=" quantity is negative;"

    # Null order_date
    df.loc[df["order_date"].isna(), "validation_error"]+=" order_date is null;"

    # Null customer_id
    df.loc[df["customer_id"].isna(), "validation_error"]+=" customer_id is null;"

    # Null order_id
    df.loc[df["order_id"].isna(), "validation_error"]+=" order_id is null;"

    # Null product_id
    df.loc[df["product_id"].isna(), "validation_error"]+=" product_id is null;"

    # Null payment_method
    df.loc[df["payment_method"].isna(), "validation_error"]+=" payment_method is null;"

    # Null status
    df.loc[df["status"].isna(), "validation_error"]+=" status is null;"



    df["validation_error"]=df["validation_error"].str.rstrip(";")

    valid=df[df["validation_error"]==""]
    valid=valid.drop(columns=["validation_error"])
    invalid=df[df["validation_error"]!=""]

    logger.info("order valid and invalid data separeated")

    return valid, invalid
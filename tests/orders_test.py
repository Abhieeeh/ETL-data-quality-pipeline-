import pandas as pd
import pytest

from validate.validate_orders import validate_orders

def test_validate_orders():
    df=pd.DataFrame({
        "order_amount":[200],
        "quantity":[2],
        "order_date":["28/2/27"],
        "customer_id":["19"],
        "order_id":["101"],
        "product_id":["201"],
        "payment_method":["upi"],
        "status":["completed"]

    })
    valid,invalid=validate_orders(df)
    assert len(invalid)==0
    assert len(valid)==1
def test_invalid_orderAmount():
    df=pd.DataFrame({
        "order_amount":[-200],
        "quantity":[2],
        "order_date":["28/2/27"],
        "customer_id":["19"],
        "order_id":["101"],
        "product_id":["201"],
        "payment_method":["upi"],
        "status":["completed"] 

    })
    valid,invalid=validate_orders(df)
    assert len(invalid)==1
    assert len(valid)==0
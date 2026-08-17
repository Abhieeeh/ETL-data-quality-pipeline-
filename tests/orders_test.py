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

def test_invalid_quantity():
    df=pd.DataFrame({
        "order_amount":[12],
        "quantity":[-1],
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

def test_payment_status():
    df=pd.DataFrame({
        "order_amount":[12],
        "quantity":[2],
        "order_date":["28/2/27"],
        "customer_id":["19"],
        "order_id":["101"],
        "product_id":["201"],
        "payment_method":["upi"],
        "status":[None] 

    })
    valid,invalid=validate_orders(df)
    assert len(invalid)==1
    assert len(valid)==0

def test_product_id():
    df=pd.DataFrame({
        "order_amount":[12],
        "quantity":[2],
        "order_date":["28/2/27"],
        "customer_id":["19"],
        "order_id":["101"],
        "product_id":[None],
        "payment_method":["upi"],
        "status":["completed"] 

    })
    valid,invalid=validate_orders(df)
    assert len(invalid)==1
    assert len(valid)==0
def test_order_id():
    df=pd.DataFrame({
        "order_amount":[12],
        "quantity":[2],
        "order_date":["28/2/27"],
        "customer_id":["19"],
        "order_id":[None],
        "product_id":["201"],
        "payment_method":["upi"],
        "status":["completed"] 

    })
    valid,invalid=validate_orders(df)
    assert len(invalid)==1
    assert len(valid)==0


def test_customer_id():
    df=pd.DataFrame({
        "order_amount":[12],
        "quantity":[2],
        "order_date":["28/2/27"],
        "customer_id":[None],
        "order_id":["101"],
        "product_id":["201"],
        "payment_method":["upi"],
        "status":["completed"] 

    })
    valid,invalid=validate_orders(df)
    assert len(invalid)==1
    assert len(valid)==0
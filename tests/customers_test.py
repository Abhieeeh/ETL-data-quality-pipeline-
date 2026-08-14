import pandas as pd
import pytest

# from validate.validate_customers import validate_customers
from validate.validate_customers import validate_customers

def test_valid_email():

    df=pd.DataFrame({
       "customer_id":[2],
       "gender":["M"],
       "first_name":["John"],
       "last_name":["Joe"],
       "address":["abcd"],
       "city":["xyz"],
       "state":["pqr"],
       "country":["ind"],
       "dob":["19/02/2001"],
       "signup_date":["25/09/2000"],
       "age":[20],
       "email":["xyz@gmail.com"],
       "phone_number":["6282316343"],
       "device_id(s)":["5485"],
       "source":["referral"]
       })
    valid,invalid=validate_customers(df)
    assert len(invalid)==0
    assert len(valid)==1


def test_invalid_email():

    df=pd.DataFrame({
       "customer_id":[2],
       "gender":["M"],
       "first_name":["John"],
       "last_name":["Joe"],
       "address":["abcd"],
       "city":["xyz"],
       "state":["pqr"],
       "country":["ind"],
       "dob":["19/02/2001"],
       "signup_date":["25/09/2000"],
       "age":[20],
       "email":["xyz"],
       "phone_number":["6282316343"],
       "device_id(s)":["5485"],
       "source":["referral"]
       })
    valid,invalid=validate_customers(df)
    assert len(invalid)==1
    assert len(valid)==0

def test_age():

    df=pd.DataFrame({
       "customer_id":[2],
       "gender":["M"],
       "first_name":["John"],
       "last_name":["Joe"],
       "address":["abcd"],
       "city":["xyz"],
       "state":["pqr"],
       "country":["ind"],
       "dob":["19/02/2001"],
       "signup_date":["25/09/2000"],
       "age":[17],
       "email":["xyz@gmail.com"],
       "phone_number":["6282316343"],
       "device_id(s)":["5485"],
       "source":["referral"]
       })
    valid,invalid=validate_customers(df)
    assert len(invalid)==1
    assert len(valid)==0

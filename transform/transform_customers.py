import pandas as pd
import re
import logging

logger=logging.getLogger(__name__)

def transform_customers(df):
    logger.info("Customer transformation completed")
    df=df.copy()

    # Remove duplicates
    n = df.duplicated().sum()
    if n > 0:
        df = df.drop_duplicates()
    

    # Checks for email pattern 
    emailpattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    df['email'] = df['email'].where(df['email'].str.match(emailpattern, na=False))

    # Remove non-numeric characters from phone_number
    df["phone_number"] = df["phone_number"].astype(str).str.replace(r"[^\d]", '', regex=True)


    # Convert dob and signup_date to datetime
    df["dob"] = pd.to_datetime(df["dob"], errors='coerce')  
    df["signup_date"] = pd.to_datetime(df["signup_date"], errors='coerce')

    return df
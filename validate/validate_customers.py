import pandas as pd
import logging

logger=logging.getLogger(__name__)

#,device_id(s),source
def validate_customers(df):
    logger.info("customers data validation started")

    df=df.copy()
    df["validation_error"]=""

    # Validate customer_id
    df.loc[df["customer_id"].isna(), "validation_error"]+=" customer_id is null;"

    # Validate gender
    df.loc[~df["gender"].isin(["M", "F", "O"]), "validation_error"]+=" gender is invalid;"

    # Validate first_name and last_name
    df.loc[df["first_name"].isna(), "validation_error"]+=" first_name is null;"
    df.loc[df["last_name"].isna(), "validation_error"]+=" last_name is null;"

    # Validate address
    df.loc[df["address"].isna(), "validation_error"]+=" address is null;"

    # Validate city, state, country
    df.loc[df["city"].isna(), "validation_error"]+=" city is null;"
    df.loc[df["state"].isna(), "validation_error"]+=" state is null;"
    df.loc[df["country"].isna(), "validation_error"]+=" country is null;"

    # Validate dob
    df.loc[df["dob"].isna(), "validation_error"]+=" dob is null;"

    # Validate signup_date
    df.loc[df["signup_date"].isna(), "validation_error"]+=" signup_date is null;"

    # Validate age
    df["age"] = (df["signup_date"]-df["dob"]).dt.days/365.25
    df.loc[df["age"]<18, "validation_error"] += "Customer is under 18;"

    # Validate email
    df.loc[df["email"].isna(), "validation_error"] += "Email is null;"

    # Validate phone number
    phone_pattern = r'^\d{2,10}$'
    df.loc[~df["phone_number"].str.match(phone_pattern,na=False), "validation_error"] += "Invalid phone number format;"

    # Validate device_id
    df.loc[df["device_id(s)"].isna(), "validation_error"] += "device_id is null;"

    # Validate source
    df.loc[df["source"].isna(), "validation_error"] += "source is null;"

    df["validation_error"]=df["validation_error"].str.rstrip(";")

    # Split valid and invalid customers
    valid = df[df["validation_error"] ==""]
    valid = valid.drop(columns=["validation_error"])
    invalid = df[df["validation_error"] != ""]
    logger.info(f"customers valid and invalid data separated, lengthof valid data :{len(valid)} and length of invalid data {len(invalid)}")


    return valid, invalid
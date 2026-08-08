import pandas as pd

#,device_id(s),source
def validate_customers(df):

    df=df.copy()
    df["Validation_error"]=""

    # Validate customer_id
    df.loc[df["customer_id"].isna(), "Validation_error"]+=" customer_id is null;"

    # Validate gender
    df.loc[~df["gender"].isin(["M", "F", "O"]), "Validation_error"]+=" gender is invalid;"

    # Validate first_name and last_name
    df.loc[df["first_name"].isna(), "Validation_error"]+=" first_name is null;"
    df.loc[df["last_name"].isna(), "Validation_error"]+=" last_name is null;"

    # Validate address
    df.loc[df["address"].isna(), "Validation_error"]+=" address is null;"

    # Validate city, state, country
    df.loc[df["city"].isna(), "Validation_error"]+=" city is null;"
    df.loc[df["state"].isna(), "Validation_error"]+=" state is null;"
    df.loc[df["country"].isna(), "Validation_error"]+=" country is null;"

    # Validate dob
    df.loc[df["dob"].isna(), "Validation_error"]+=" dob is null;"

    # Validate signup_date
    df.loc[df["signup_date"].isna(), "Validation_error"]+=" signup_date is null;"

    # Validate age
    df["age"] = (df["signup_date"]-df["dob"]).dt.days/365.25
    df.loc[df["age"]<18, "Validation_error"] += "Customer is under 18;"

    # Validate email
    df.loc[df["email"].isna(), "Validation_error"] += "Email is null;"

    # Validate phone number
    phone_pattern = r'^\d{2,10}$'
    df.loc[~df["phone_number"].str.match(phone_pattern,na=False), "Validation_error"] += "Invalid phone number format;"

    # Validate device_id
    df.loc[df["device_id(s)"].isna(), "Validation_error"] += "device_id is null;"

    # Validate source
    df.loc[df["source"].isna(), "Validation_error"] += "source is null;"

    df["Validation_error"]=df["Validation_error"].str.rstrip(";")

    # Split valid and invalid customers
    valid = df[df["Validation_error"] ==""]
    valid = valid.drop(columns=["Validation_error"])
    invalid = df[df["Validation_error"] != ""]

    return valid, invalid
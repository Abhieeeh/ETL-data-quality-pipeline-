import pandas as pd

def validate_customers(df):
    valid=df.copy()
    invalid=pd.DataFrame()

    # Validate age
    age = (valid["signup_date"]-valid["dob"]).dt.days/365.25
    invalid_age=valid[age<18]
    invalid["age_validation_error"]="Customer is under 18"
    invalid=pd.concat([invalid, invalid_age])

    # Validate email
    invalid_email=df["email"].isna()
    invalid["email_validation_error"]="Invalid email format"
    invalid=pd.concat([invalid, invalid_email])

    # Validate phone number
    phone_pattern = r'^\d{2,10}$'
    invalid_phone=valid[~valid['phone_number'].str.match(phone_pattern,na=False)]
    invalid["phone_validation_error"]="Invalid phone number format"
    invalid=pd.concat([invalid, invalid_phone])


    emailpattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    valid=valid[
        (age>=18) &
        (valid['email'].str.match(emailpattern,na=False)) &
        (valid['phone_number'].str.match(phone_pattern,na=False))
    ]

    return valid, invalid
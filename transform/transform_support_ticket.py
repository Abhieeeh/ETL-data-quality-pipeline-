import pandas as pd

def transform_support_ticket(df):

    df=df.copy()

    #drop duplicates

    n=df.duplicated().sum()
    if n>0:
        df.drop_duplicates()


    # convert date columns into date and time format 

    df["ticket_created"]=pd.to_datetime(df["ticket_created"],errors="coerce")
    df["ticket_resolved"]=pd.to_datetime(df["ticket_resolved"],errors="coerce")

    return df


    


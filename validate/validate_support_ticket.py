import pandas as pd
import logging

logger=logging.getLogger(__name__)

def validate_support_ticket(df):
    logger.info("support tickets data validation started")
    df=df.copy()

    df["validation_error"]=""

    # Validate ticket_id
    df.loc[df["ticket_id"].isna(), "validation_error"]+=" ticket_id is null;"

    # Validate customer_id
    df.loc[df["customer_id"].isna(), "validation_error"]+=" customer_id is null;"

    # Validate issue_type
    df.loc[df["issue_type"].isna(), "validation_error"]+=" issue_type is null;"

    # Validate ticket_created
    df.loc[df["ticket_created"].isna(), "validation_error"]+=" ticket_created date is null;"

    # Validate ticket_resolved
    df.loc[df["ticket_resolved"].isna(), "validation_error"]+=" ticket_resolved date is null;"

    # Validate support_agent
    df.loc[df["support_agent"].isna(), "validation_error"]+=" support_agent is null;"

    # Validate sentiment
    df.loc[df["sentiment"].isna(), "validation_error"]+=" sentiment is null;"

    # Validate resolution_time_hours
    df.loc[df["resolution_time_hours"].isna(), "validation_error"]+=" resolution_time_hours is null;"

    # Validate resolution_time_hours negative
    df.loc[df["resolution_time_hours"]<0, "validation_error"]+=" resolution_time_hours is negative;"

    # Validate ticket_resolved date is not earlier than ticket_created date
    df.loc[df["ticket_resolved"]<df["ticket_created"], "validation_error"]+=" ticket_resolved date is earlier than ticket_created date;"

    df["validation_error"]=df["validation_error"].str.rstrip(";")


    # Split valid and invalid support tickets
    valid=df[df["validation_error"]==""]
    valid=valid.drop(columns=["validation_error"])
    invalid=df[df["validation_error"]!=""]

    logger.info(f"support tickets valid and invalid data separeated, lengthof valid data :{len(valid)} and length of invalid data {len(invalid)}")

    return valid, invalid
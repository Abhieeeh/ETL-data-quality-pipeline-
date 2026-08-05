import pandas as pd

def validate_support_ticket(df):
    valid=df.copy()
    invalid=pd.DataFrame()


    nullcreatedates=df[df["ticket_created"].isna()]
    invalid["date_created_error"]="Ticket created date is null"
    invalid=pd.concat([invalid, nullcreatedates])

    nullresolvedates=df[df["ticket_resolved"].isna()]
    invalid["date_resolved_error"]="Ticket resolved date is null"
    invalid=pd.concat([invalid, nullresolvedates])

    invalid_dates=((df["ticket_resolved"]<df["ticket_created"])).astype(int)
    invalidDates=valid[invalid_dates==1]
    invalid["date_validation_error"]="Ticket resolved date is earlier than ticket created date"
    invalid=pd.concat([invalid, invalidDates])

    
    valid=df[(
        df["ticket_created"].notna()) &
        (df["ticket_resolved"].notna()) &
        (df["ticket_resolved"]>=df["ticket_created"]
    )]

    

    return valid, invalid
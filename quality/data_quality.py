import pandas as pd
import logging

logger=logging.getLogger("__name__")

def check_data_quality():
    logger.info("data quality pipeline started")
    
    customers=pd.read_csv("./data/raw/customers.csv ")
    logger.info(f"customer data loaded for quality check, length : {len(customers)}")
    order=pd.read_csv("./data/raw/orders.csv")
    logger.info(f"order data loaded for quality check, length : {len(order)}")
    tickets=pd.read_csv("./data/raw/support_tickets.csv")
    logger.info(f"ticket data loaded for quality check, length : {len(tickets)}")
    validOrders=pd.read_csv("./data/processed/valid_orders.csv")
    logger.info(f"valid orders data loaded for quality check, length : {len(validOrders)}")
    invalidOrders=pd.read_csv("./data/invalid/invalid_orders.csv")
    logger.info(f"invalid orders data loaded for quality check, length : {len(invalidOrders)}")
    validCustomers=pd.read_csv("./data/processed/valid_customers.csv")
    logger.info(f"valid customers data loaded for quality check, length : {len(validCustomers)}")
    invalidCustomers=pd.read_csv("./data/invalid/invalid_customers.csv")
    logger.info(f"invalid customers data loaded for quality check, length : {len(invalidCustomers)}")
    validSupportTicket=pd.read_csv("./data/processed/valid_tickets.csv")
    logger.info(f"valid support ticket data loaded for quality check, length : {len(validSupportTicket)}")
    invalidSupportTicket=pd.read_csv("./data/invalid/invalid_tickets.csv")
    logger.info(f"invalid support ticket data loaded for quality check, length : {len(invalidSupportTicket)}")


    data_quality_report = pd.DataFrame({
    "Dataset": ["Orders", "Customers", "Support Tickets"],
    "Total": [
        len(order),
        len(customers),
        len(tickets)
    ],
    "Valid": [
        len(validOrders),
        len(validCustomers),
        len(validSupportTicket)
    ],
    "Invalid": [
        len(invalidOrders),
        len(invalidCustomers),
        len(invalidSupportTicket)
    ],
    "Valid %":[
        (len(validOrders)/len(order))*100,
        (len(validCustomers)/len(customers))*100,
        (len(validSupportTicket)/len(tickets))*100
    ]
    })

    data_quality_report.to_csv("./reports/data_quality_report.csv",index=False)
    logger.info(f"data quality report save to the directory reports, path : /reports/data_quality_report.csv")
   
def error_count(path,dataset):
    df=pd.read_csv(path)
    error=(
        df["validation_error"]
        .str.split(";")
        .explode()
        .str.strip())
    error=pd.DataFrame(error)
    error=error[error!=""]
    count=error.groupby("validation_error").size().values
    index=error.groupby("validation_error").size().index
    error_details=pd.DataFrame({
    "Dataset":dataset,
    "Error":index,
    "count":count
    })
    logger.info("data quality report prepared")
    error_details.to_csv(f"./reports/{dataset}_error_details.csv",index=False)
    logger.info(f"data quality,error count of {dataset} saved as csv, path : /reports/{dataset}_error_details.csv")
    

    


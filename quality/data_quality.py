import pandas as pd

def check_data_quality():
    
    customers=pd.read_csv("./data/raw/customers.csv ")
    order=pd.read_csv("./data/raw/orders.csv")
    tickets=pd.read_csv("./data/raw/support_tickets.csv")
    validOrders=pd.read_csv("./data/processed/valid_orders.csv")
    invalidOrders=pd.read_csv("./data/invalid/invalid_orders.csv")
    validCustomers=pd.read_csv("./data/processed/valid_customers.csv")
    invalidCustomers=pd.read_csv("./data/invalid/invalid_customers.csv")
    validSupportTicket=pd.read_csv("./data/processed/valid_tickets.csv")
    invalidSupportTicket=pd.read_csv("./data/invalid/invalid_tickets.csv")


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
    error_details.to_csv(f"./reports/{dataset}_error_details.csv",index=False)
    

    


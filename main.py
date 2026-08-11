from extract.extract import extract_orders
from transform.transform_orders import transform_orders
from validate.validate_orders import validate_orders

from extract.extract import extract_customers
from transform.transform_customers import transform_customers
from validate.validate_customers import validate_customers

from extract.extract import extract_support_tickets
from transform.transform_support_ticket import transform_support_ticket
from validate.validate_support_ticket import validate_support_ticket

from quality.data_quality import check_data_quality
from quality.data_quality import error_count

def run_orders_pipeline(path):
    # Extract
    orders=extract_orders(path)
    # Transform
    orders=transform_orders(orders)
    # Validate
    valid_orders, invalid_orders=validate_orders(orders)
    # Save the valid and invalid orders to separate CSV files
    valid_orders.to_csv("./data/processed/valid_orders.csv", index=False)
    invalid_orders.to_csv("./data/invalid/invalid_orders.csv", index=False)
   
def run_customers_pipeline(path):
    # Extract
    customers=extract_customers(path)
    
    # Transform
    customers=transform_customers(customers)
    
    # Validate
    valid_customers, invalid_customers=validate_customers(customers)
    
    # Save the valid and invalid customers to separate CSV files
    valid_customers.to_csv("./data/processed/valid_customers.csv", index=False)
    invalid_customers.to_csv("./data/invalid/invalid_customers.csv", index=False)

def run_SupportTicket_pipeline(path):
    # Extract
    tickets=extract_support_tickets(path)
    
    # Transform
    tickets=transform_support_ticket(tickets)
    
    # Validate
    valid_ticket, invalid_ticket=validate_support_ticket(tickets)
    
    # Save the valid and invalid customers to separate CSV files
    valid_ticket.to_csv("./data/processed/valid_tickets.csv", index=False)
    invalid_ticket.to_csv("./data/invalid/invalid_tickets.csv", index=False)


run_orders_pipeline("./data/raw/orders.csv")
run_customers_pipeline("./data/raw/customers.csv")
run_SupportTicket_pipeline("./data/raw/support_tickets.csv")
check_data_quality()
error_count("./data/invalid/invalid_customers.csv","Customers")
error_count("./data/invalid/invalid_orders.csv","Orders")
error_count("./data/invalid/invalid_tickets.csv","Support_ticket")

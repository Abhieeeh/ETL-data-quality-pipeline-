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

import logging

def logging_data():
    logging.basicConfig(
    filename="./logs/etl_pipeline.log",
    level=logging.INFO,
    format="%(asctime)s-%(levelname)s-%(message)s"
)
logging_data()
logger=logging.getLogger(__name__)


def run_orders_pipeline(path):
    logger.info("order pipeline started")

    # Extract
    orders=extract_orders(path)
    logger.info("order extraction completed")

    # Transform
    orders=transform_orders(orders)
    logger.info("order data transformation completed")

    # Validate
    valid_orders, invalid_orders=validate_orders(orders)
    logger.info("orders data validation completed")

    # Save the valid and invalid orders to separate CSV files
    valid_orders.to_csv("./data/processed/valid_orders.csv", index=False)
    logger.info("valid orders data saved as csv, path :/data/processed/valid_orders.csv")
    invalid_orders.to_csv("./data/invalid/invalid_orders.csv", index=False)
    logger.info("invalid orders data saved as csv, path :/data/invalid/invalid_orders.csv")
   
def run_customers_pipeline(path):
    logger.info("customers pipeline started")

    # Extract
    customers=extract_customers(path)
    logger.info("customers extraction completed")
    
    # Transform
    customers=transform_customers(customers)
    logger.info("customers data transformation completed")

    # Validate
    valid_customers, invalid_customers=validate_customers(customers)
    logger.info("customers data validation completed")
    
    # Save the valid and invalid customers to separate CSV files
    valid_customers.to_csv("./data/processed/valid_customers.csv", index=False)
    logger.info("valid customers data saved as csv, path :/data/processed/valid_customers.csv")
    invalid_customers.to_csv("./data/invalid/invalid_customers.csv", index=False)
    logger.info("invalid customers data saved as csv, path :/data/invalid/invalid_customers.csv")

def run_SupportTicket_pipeline(path):
    
    logger.info("support tickets pipeline started")

    # Extract
    tickets=extract_support_tickets(path)
    logger.info("support ticket extraction completed")

    # Transform
    tickets=transform_support_ticket(tickets)
    logger.info("support tickets data transformation completed")

    # Validate
    valid_ticket, invalid_ticket=validate_support_ticket(tickets)
    logger.info("support ticket data validation completed")

    # Save the valid and invalid customers to separate CSV files
    valid_ticket.to_csv("./data/processed/valid_tickets.csv", index=False)
    logger.info("valid support tickets data saved as csv, path :/data/processed/valid_tickets.csv")
    invalid_ticket.to_csv("./data/invalid/invalid_tickets.csv", index=False)
    logger.info("invalid support tickets data saved as csv, path :/data/invalid/invalid_tickets.csv")

def run_pipeline():
    run_orders_pipeline("./data/raw/orders.csv")
    run_customers_pipeline("./data/raw/customers.csv")
    run_SupportTicket_pipeline("./data/raw/support_tickets.csv")

def quality_report():
    check_data_quality()
    error_count("./data/invalid/invalid_customers.csv","Customers")
    error_count("./data/invalid/invalid_orders.csv","Orders")
    error_count("./data/invalid/invalid_tickets.csv","Support_ticket")


run_pipeline()
quality_report()


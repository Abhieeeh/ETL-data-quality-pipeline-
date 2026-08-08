from extract.extract import extract_orders
from transform.transform_orders import transform_orders
from validate.validate_orders import validate_orders

from extract.extract import extract_customers
from transform.transform_customers import transform_customers
from validate.validate_customers import validate_customers

from extract.extract import extract_support_ticket
from transform.transform_support_ticket import transform_support_ticket
from validate.validate_support_ticket import validate_support_ticket



# ORDERS

# Extract
orders=extract_orders("./data/raw/orders.csv")

# Transform
orders=transform_orders(orders)

# Validate
valid_orders, invalid_orders=validate_orders(orders)

# Save the valid and invalid orders to separate CSV files
valid_orders.to_csv("./data/processed/valid_orders.csv", index=False)
invalid_orders.to_csv("./data/invalid/invalid_orders.csv", index=False)



# CUSTOMERS

# Extract
customers=extract_customers("./data/raw/customers.csv")

# Transform
customers=transform_customers(customers)

# Validate
valid_customers, invalid_customers=validate_customers(customers)

# Save the valid and invalid customers to separate CSV files
valid_customers.to_csv("./data/processed/valid_customers.csv", index=False)
invalid_customers.to_csv("./data/invalid/invalid_customers.csv", index=False)



# SUPPORT TICKETS

# Extract
tickets=extract_support_ticket("./data/raw/support_tickets.csv")

# Transform
tickets=transform_support_ticket(tickets)

# Validate
valid_tickets, invalid_tickets=validate_support_ticket(tickets)

# Save the valid and invalid support tickets to separate CSV files
valid_tickets.to_csv("./data/processed/valid_support_tickets.csv", index=False)
invalid_tickets.to_csv("./data/invalid/invalid_support_tickets.csv", index=False)

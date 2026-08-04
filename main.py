from extract.extract import extract_orders
from transform.transform_orders import transform_orders
from validate.validate_orders import validate_orders

# Extract
orders=extract_orders("./data/raw/orders.csv")

# Transform
orders=transform_orders(orders)

# Validate
valid_orders, invalid_orders=validate_orders(orders)

# Save the valid and invalid orders to separate CSV files
valid_orders.to_csv("./data/processed/valid_orders.csv", index=False)
invalid_orders.to_csv("./data/invalid/invalid_orders.csv", index=False)
import pandas as pd
import logging

logger=logging.getLogger(__name__)

def extract_orders(path):
    try:
        data= pd.read_csv(path)
        logger.info(f"Orders data extracted, length : {len(data)}")
        return data
    except Exception:
        logger.exception("Orders extraction failed")
    

    
def extract_customers(path):
    try:
        data = pd.read_csv(path)
        logger.info(f"Customers data extracted{len(data)}")
        return data

    except Exception:
        logger.exception("Customers Extraction failed")

    


def extract_support_tickets(path):
    try:
        data = pd.read_csv(path)
        logger.info(f"Support ticket data extracted")
        return data
    except Exception:
        logger.exception("Support ticket data extraction failed")


    
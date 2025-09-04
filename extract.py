'''1. Processing customer data from a CSV file for a retail company to ensure clean, unique records.
Tasks involved: Deduplication, Cleaning
CSV file: This is a common file format containing customer data like names, addresses, phone numbers, emails, etc.
Deduplication: This means identifying and removing duplicate customer records. based on the customer id, you aim to keep only one clean version.
Cleaning: This includes fixing errors in the data — such as correcting typos, standardizing formats (like dates or phone numbers), filling in missing values, or removing invalid records.
🟢 Goal: Ensure that the customer database is accurate, standardized, and contains only one record per customer.'''


import pandas as pd

def read_data():
    raw_data=pd.read_csv("us_customer_data 3.csv")
    return raw_data

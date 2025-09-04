import pandas as pd
from sqlalchemy import create_engine,text
import configparser 
from sqlalchemy.engine import URL
import urllib

def connect_to_ssmss():
    config = configparser.ConfigParser()
    config.read(r'C:\Users\Ananya\OneDrive\Desktop\vs.code\config.config')
 
    DRIVER = config['ssms']['DRIVER']
    SERVER = config['ssms']['SERVER']
    DATABASE = config['ssms']['DATABASE']
    UID = config['ssms']['UID']
    PWD = config['ssms']['PWD']
 
    
    connect_str = (f'DRIVER={DRIVER};'
               f'SERVER={SERVER};'
               f'DATABASE={DATABASE};'
               f'UID={UID};'
               f'PWD={PWD};'
               'Encrypt=no;'
               'TrustServerCertificate=yes;')

   
    params = urllib.parse.quote_plus(connect_str)
    engine = create_engine(f'mssql+pyodbc:///?odbc_connect={params}')
 
    return engine
 

def insert_data(df , table_name):
        df.to_sql(name=table_name, con=connect_to_ssmss(), if_exists='replace', index=False)
        return f" Data inserted into table: {table_name}"
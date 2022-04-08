import pandas as pd
from sqlalchemy import create_engine

# Read the excel file and print a few of the records to make sure they look right
df = pd.read_excel ('assets/20210309_2020_1 - 4.xls')
print (df.head())

# Connect to the database
engine = create_engine('sqlite:///ohio-quarterly.db')

# Create the table
df.to_sql('OhioWells', engine)


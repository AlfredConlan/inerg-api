import pandas as pd
from sqlalchemy import create_engine

df = pd.read_excel ('assets/20210309_2020_1 - 4.xls')
print (df.head())

engine = create_engine('sqlite:///ohio-quarterly.db')

df.to_sql('OhioWells', engine)


import sqlite3 as sql
import pandas as pd

conn = sql.connect('results.db')
results = pd.read_sql('SELECT * FROM allresults', conn)
car_type = pd.read_sql('SELECT car_type FROM allresults', conn)
price = pd.read_sql('SELECT price_per_day FROM allresults', conn)

for row in results:
    print(car_type, price)

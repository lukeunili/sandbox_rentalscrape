import sqlite3
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "results.db")

Connection = sqlite3.connect(db_path)
Cursor = Connection.cursor()
Cursor.execute("Select car_type, price_per_day, pickuptime, dropofftime, mileage FROM allresults ORDER BY price_per_day +0 asc")
View = Cursor.fetchall()
print(View)
Connection.close()

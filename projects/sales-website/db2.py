import sqlite3
import json

db = sqlite3.connect("data.db")
cursor = db.cursor()
cursor.execute("SELECT products FROM carts")
product = cursor.fetchone()
print(type(product[0]))
# json.load(file)
product = json.loads(product[0])
print(type(product))

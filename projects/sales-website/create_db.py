import sqlite3
import httpx
import json


db = sqlite3.connect("data.db")
cursor = db.cursor()
cursor.execute(
    """CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY NOT NULL,
            title TEXT NOT NULL,
            description TEXT,
            price REAL,
            category TEXT,
            image TEXT
)"""
)

cursor.execute(
    """CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY NOT NULL,
            email TEXT,
            username TEXT,
            password TEXT
)"""
)

cursor.execute("""CREATE TABLE IF NOT EXISTS carts (
                user_id INTEGER PRIMARY KEY NOT NULL,
                products TEXT,
                purchase_date TEXT
)""")


url = "https://fakestoreapi.com/products"
response = httpx.get(url)
data = response.json()

for product in data:
    cursor.execute(
        """INSERT INTO products
                (id, title, description, price, category, image)
                VALUES (?, ?, ?, ?, ?, ?)""",
        [
            product["id"],
            product["title"],
            product["description"],
            product["price"],
            product["category"],
            product["image"],
        ],
    )


response = httpx.get("https://fakestoreapi.com/users")
data = response.json()
for user in data:
    cursor.execute(
        "INSERT INTO users (id, email, username, password) VALUES (?, ?, ?, ?)",
        [user["id"], user["email"], user["username"], user["password"]],
    )

db.commit()

user_id = 3
products = {6: 4, 7: 10, 1: 1}

# json.dump(products, file)
products_json = json.dumps(products)  # "[6, 7, 8, 20]"

cursor.execute("INSERT INTO carts (user_id, products) VALUES (?, ?)", [1, products_json])
cursor.execute("INSERT INTO carts (user_id, products) VALUES (?, ?)", [2, products_json])
cursor.execute("INSERT INTO carts (user_id, products) VALUES (?, ?)", [3, products_json])
cursor.execute("INSERT INTO carts (user_id, products) VALUES (?, ?)", [4, products_json])
cursor.execute("INSERT INTO carts (user_id, products) VALUES (?, ?)", [5, products_json])
cursor.execute("INSERT INTO carts (user_id, products) VALUES (?, ?)", [6, products_json])
cursor.execute("INSERT INTO carts (user_id, products) VALUES (?, ?)", [7, products_json])
cursor.execute("INSERT INTO carts (user_id, products) VALUES (?, ?)", [8, products_json])
db.commit()

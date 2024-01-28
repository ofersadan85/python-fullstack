import sqlite3
import httpx

db = sqlite3.connect("data.db")
cursor = db.cursor()

url = "https://fakestoreapi.com/products"
response = httpx.get(url)
data = response.json()

cursor.execute(
    """CREATE TABLE products (
               id INTEGER PRIMARY KEY NOT NULL,
               title TEXT NOT NULL,
               description TEXT,
               price REAL,
               category TEXT,
               image TEXT
)"""
)

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

cursor.execute("""CREATE TABLE users (
               id INTEGER PRIMARY KEY NOT NULL,
               email TEXT,
               username TEXT,
               password TEXT
)""")

response = httpx.get("https://fakestoreapi.com/users")
data = response.json()
for user in data:
    cursor.execute("INSERT INTO users (id, email, username, password) VALUES (?, ?, ?, ?)",
                   [
                       user["id"],
                       user["email"],
                       user["username"],
                       user["password"]
                   ])


db.commit()

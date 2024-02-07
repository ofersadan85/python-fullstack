
class Product:
    def __init__(self, id, title, description, price, image):
        self.id = id
        self.title = title
        self.description = description
        self.price = price
        self.image = image


class ProductCreate:
    def __init__(self, title, description, price, image):
        self.title = title
        self.description = description
        self.price = price
        self.image = image

    def create(self, cursor):
        params = [self.title, self.description, self.price, self.image]
        cursor.execute("""INSERT INTO products (title, description, price, image)
                       VALUES (?, ?, ?, ?)""", params)
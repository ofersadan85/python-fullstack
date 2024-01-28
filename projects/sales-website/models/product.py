from dataclasses import dataclass


@dataclass
class ProductCreate:
    title: str
    price: float
    description: str
    image: str
    # amount: int
    # category: str

    def add_product_to_db(self) -> int:
        # cursor.execute("INSERT...")
        pass


@dataclass
class Product(ProductCreate):
    id: int

    def add_product_to_db(self):
        raise TypeError("Tried to create existing product")

    @classmethod
    def get_list_of_products(cls) -> list["Product"]:
        # Logic to bring the list from the DB
        # product = Product(*args)
        # product = Product(**kwargs)
        return [Product(123, "cup of tea", 500.0, 1000, "the best cup of tea")]

    @classmethod
    def get_product_by_id(cls, id) -> "Product":
        return Product(id, "cup of tea", 500.0, 1000, "the best cup of tea")

    def update_product_in_db(self) -> "Product":
        return Product(123, "cup of tea", 50.0, 1000, "the best cup of tea")

    def delete_product_from_db(self) -> bool:
        # "DELETE FROM products WHERE id = ?, [self.id]"
        return True

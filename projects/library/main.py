class Library:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.books = []
        self.employees = []
        self.customers = []


class Book:
    def __init__(self, title, author, year, genre, language):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.language = language


class Customer:
    pass

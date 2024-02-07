
class User:
    def __init__(self, id, username, email):
        self.id = id
        self.username = username
        self.email = email


class UserCreate:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def create(self, cursor):
        params = [self.username, self.password, self.email]
        cursor.execute(
            "INSERT INTO users (username, password, email) VALUES (?, ?, ?)", params
        )
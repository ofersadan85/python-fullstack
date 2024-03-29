CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY NOT NULL,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    email TEXT,
    age INTEGER,
    role TEXT NOT NULL DEFAULT 'user'
);
INSERT INTO users (username, password, email, age, role)
VALUES ('admin', '1234', 'admin@mysite.com', 30, 'admin'),
    ('user', '1234', 'user@mysite.com', 25, 'user');
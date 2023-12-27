DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    email TEXT,
    first_name TEXT,
    last_name TEXT
);

INSERT INTO
    users (username, password)
VALUES
    ('admin', '1234');

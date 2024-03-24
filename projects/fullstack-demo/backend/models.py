from dataclasses import dataclass


@dataclass
class User:
    id: int
    username: str
    password: str
    email: str | None = None
    age: int | None = None


@dataclass
class PublicUser:
    id: int
    username: str
    email: str | None = None
    age: int | None = None


@dataclass
class NewUser:
    username: str
    password: str
    email: str | None = None
    age: int | None = None

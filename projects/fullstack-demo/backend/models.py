from dataclasses import dataclass


@dataclass
class PublicUser:
    id: int
    username: str
    role: str
    email: str | None = None
    age: int | None = None

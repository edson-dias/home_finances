from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class User:
    name: str
    email: str
    password: str
    username: str
    created_at: datetime
    id: Optional[int] = None
    reference: Optional[str] = None

    def __hash__(self):
        return hash(self.reference)

    def __str__(self) -> str:
        return self.name

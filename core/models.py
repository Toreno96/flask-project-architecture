import dataclasses
import itertools
from typing import Optional


class ValidationError(Exception):
    pass


class NotFound(Exception):
    pass


_model_user_id = itertools.count(3)


@dataclasses.dataclass
class User:
    email: str
    username: str
    id: Optional[int] = None

    def full_clean(self):
        errors = []
        if self.email in [i.email for i in MODEL_USERS_IN_DB]:
            errors.append(
                {
                    "loc": "email",
                    "value": self.email,
                    "details": "user with this email already exists",
                }
            )
        if self.username in [i.username for i in MODEL_USERS_IN_DB]:
            errors.append(
                {
                    "loc": "username",
                    "value": self.username,
                    "details": "user with this username already exists",
                }
            )
        if errors:
            raise ValidationError(self, errors)

    def save(self):
        self.full_clean()
        self.id = next(_model_user_id)
        MODEL_USERS_IN_DB.append(self)


MODEL_USERS_IN_DB = [
    User(id=1, email="foo@example.com", username="foo42"),
    User(id=2, email="bar@example.com", username="bar24"),
]

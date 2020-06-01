import dataclasses
import itertools


class ModelValidationError(Exception):
    pass


class ModelNotFound(Exception):
    pass


_model_user_id = itertools.count(1)


@dataclasses.dataclass
class ModelUser:
    email: str
    username: str
    id: int = dataclasses.field(default_factory=lambda: next(_model_user_id))

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
            raise ModelValidationError(self, errors)

    def save(self):
        self.full_clean()
        MODEL_USERS_IN_DB.append(self)


MODEL_USERS_IN_DB = [
    ModelUser(email="foo@example.com", username="foo42"),
    ModelUser(email="bar@example.com", username="hax0rBAAR"),
]

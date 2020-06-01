from core import models


def user_create(*, email: str, username: str) -> models.User:
    user = models.User(email=email, username=username)
    user.save()
    return user

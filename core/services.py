from core import models


def service_user_create(*, email: str, username: str) -> models.ModelUser:
    user = models.ModelUser(email=email, username=username)
    user.save()
    return user

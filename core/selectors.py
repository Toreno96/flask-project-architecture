import typing

from core import models


def selector_user_list() -> typing.List[models.ModelUser]:
    return MODEL_USERS_IN_DB


def selector_user_detail(*, user_id: int) -> models.ModelUser:
    try:
        return next(i for i in models.MODEL_USERS_IN_DB if i.id == user_id)
    except StopIteration:
        raise models.ModelNotFound(models.ModelUser, user_id)

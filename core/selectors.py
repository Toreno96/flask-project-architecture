import typing

from core import models


def user_list() -> typing.List[models.User]:
    return models.MODEL_USERS_IN_DB


def user_detail(*, user_id: int) -> models.User:
    try:
        return next(i for i in models.MODEL_USERS_IN_DB if i.id == user_id)
    except StopIteration:
        raise models.NotFound(models.User, user_id)

import dataclasses
import http

import flask
import pydantic

from core import models
from core import schemas
from core import selectors
from core import services

# Flask app definition

app = flask.Flask(__name__)


# Exception handling


@app.errorhandler(pydantic.error_wrappers.ValidationError)
def handle_schema_validation_error(e):
    return {"errors": e.errors()}, http.HTTPStatus.BAD_REQUEST


@app.errorhandler(models.ValidationError)
def handle_schema_validation_error(e):
    return flask.jsonify({"errors": e.args[1]}), http.HTTPStatus.BAD_REQUEST


@app.errorhandler(models.NotFound)
def handle_schema_validation_error(e):
    return flask.jsonify({"errors": e.args[1]}), http.HTTPStatus.NOT_FOUND


# URLs + APIs

USER_PATH = "/users"


@app.route(f"{USER_PATH}/create", methods=["POST"])
def user_create_api():
    body = flask.request.get_json()
    if not isinstance(body, dict):
        body = {}

    deserialized = schemas.UserCreateInput(**body)
    user = services.user_create(**deserialized.dict())
    output = schemas.UserCreateOutput(**dataclasses.asdict(user)).dict()

    return flask.jsonify(output), http.HTTPStatus.CREATED


@app.route(f"{USER_PATH}", methods=["GET"])
def user_list_api():
    users = selectors.user_list()
    output = [schemas.UserListOutput(**dataclasses.asdict(i)).dict() for i in users]

    return flask.jsonify(output), http.HTTPStatus.OK


@app.route(f"{USER_PATH}/<user_id>", methods=["GET"])
def user_detail_api(user_id):
    user_id = int(user_id)
    user = selectors.user_detail(user_id=user_id)
    output = schemas.UserDetailOutput(**dataclasses.asdict(user)).dict()

    return flask.jsonify(output), http.HTTPStatus.OK

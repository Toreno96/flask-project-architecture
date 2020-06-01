import dataclasses
import http

import flask


# Flask app definition

app = flask.Flask(__name__)


# Exception handling


@app.errorhandler(pydantic.error_wrappers.ValidationError)
def handle_schema_validation_error(e):
    return {"errors": e.errors()}, http.HTTPStatus.BAD_REQUEST


@app.errorhandler(ModelValidationError)
def handle_schema_validation_error(e):
    return flask.jsonify({"errors": e.args[1]}), http.HTTPStatus.BAD_REQUEST


@app.errorhandler(ModelNotFound)
def handle_schema_validation_error(e):
    return flask.jsonify({"errors": e.args[1]}), http.HTTPStatus.NOT_FOUND


# URLs + APIs

USER_PATH = "/users"


@app.route(f"{USER_PATH}/create", methods=["POST"])
def user_create_api():
    body = flask.request.get_json()
    if not isinstance(body, dict):
        body = {}

    deserialized = SchemaUserCreateInput(**body)
    user = service_user_create(**deserialized.dict())
    output = SchemaUserCreateOutput(**dataclasses.asdict(user)).dict()

    return flask.jsonify(output), http.HTTPStatus.CREATED


@app.route(f"{USER_PATH}", methods=["GET"])
def user_list_api():
    users = selector_user_list()
    output = [SchemaUserListOutput(**dataclasses.asdict(i)).dict() for i in users]

    return flask.jsonify(output), http.HTTPStatus.OK


@app.route(f"{USER_PATH}/<user_id>", methods=["GET"])
def user_detail_api(user_id):
    user_id = int(user_id)
    user = selector_user_detail(user_id=user_id)
    output = SchemaUserDetailOutput(**dataclasses.asdict(user)).dict()

    return flask.jsonify(output), http.HTTPStatus.OK

from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import passengers_controller
from t08_flask_mysql.app.my_project.auth.domain.orders.passengers import Passengers

passengers_bp = Blueprint('passengers', __name__, url_prefix='/passengers')


@passengers_bp.get('')
def get_all_passengers() -> Response:
    return make_response(jsonify(passengers_controller.find_all()), HTTPStatus.OK)


@passengers_bp.get('/<int:id>')
def get_passengers(id: int) -> Response:
    return make_response(jsonify(passengers_controller.find_by_id(id)), HTTPStatus.OK)


@passengers_bp.post('')
def post_passengers() -> Response:
    json = request.get_json()
    passengers = Passengers.create_from_dto(json)
    passengers_controller.create(passengers)
    return make_response(jsonify(passengers.put_into_dto()), HTTPStatus.OK)


@passengers_bp.put('/<int:id>')
def put_passengers(id: int) -> Response:
    json = request.get_json()
    passengers = Passengers.create_from_dto(json)
    passengers_controller.update(id, passengers)
    return make_response("Passengers Updated", HTTPStatus.OK)


@passengers_bp.patch('/<int:id>')
def patch_passengers(id: int) -> Response:
    json = request.get_json()
    passengers_controller.patch(id, json)
    return make_response("Passengers Patched", HTTPStatus.OK)


@passengers_bp.delete('/<int:id>')
def delete_passengers(id: int) -> Response:
    passengers_controller.delete(id)
    return make_response("Passengers Deleted", HTTPStatus.OK)

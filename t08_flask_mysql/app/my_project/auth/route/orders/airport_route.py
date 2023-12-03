from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import airport_controller
from t08_flask_mysql.app.my_project.auth.domain.orders.airport import Airport

airport_bp = Blueprint('airport', __name__, url_prefix='/airports')


@airport_bp.get('')
def get_all_airport() -> Response:
    return make_response(jsonify(airport_controller.find_all()), HTTPStatus.OK)


@airport_bp.get('/<int:id>')
def get_airport(id: int) -> Response:
    return make_response(jsonify(airport_controller.find_by_id(id)), HTTPStatus.OK)


@airport_bp.post('')
def post_airport() -> Response:
    json = request.get_json()
    airport = Airport.create_from_dto(json)
    airport_controller.create(airport)
    return make_response(jsonify(airport.put_into_dto()), HTTPStatus.OK)


@airport_bp.put('/<int:id>')
def put_airports(id: int) -> Response:
    json = request.get_json()
    airport = Airport.create_from_dto(json)
    airport_controller.update(id, airport)
    return make_response("Airport Updated", HTTPStatus.OK)


@airport_bp.patch('/<int:id>')
def patch_airports(id: int) -> Response:
    json = request.get_json()
    airport_controller.patch(id, json)
    return make_response("Airport Patched", HTTPStatus.OK)


@airport_bp.delete('/<int:id>')
def delete_airport(id: int) -> Response:
    airport_controller.delete(id)
    return make_response("Airport Deleted", HTTPStatus.OK)

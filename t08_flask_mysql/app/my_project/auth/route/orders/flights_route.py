from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import flights_controller
from t08_flask_mysql.app.my_project.auth.domain.orders.flight import Flight

flights_bp = Blueprint('flights', __name__, url_prefix='/flights')


@flights_bp.get('')
def get_all_flights() -> Response:
    return make_response(jsonify(flights_controller.find_all()), HTTPStatus.OK)


@flights_bp.get('/<int:id>')
def get_flights(id: int) -> Response:
    return make_response(jsonify(flights_controller.find_by_id(id)), HTTPStatus.OK)


@flights_bp.post('')
def post_flights() -> Response:
    json = request.get_json()
    flights = Flight.create_from_dto(json)
    flights_controller.create(flights)
    return make_response(jsonify(flights.put_into_dto()), HTTPStatus.OK)


@flights_bp.put('/<int:id>')
def put_flights(id: int) -> Response:
    json = request.get_json()
    flights = Flight.create_from_dto(json)
    flights_controller.update(id, flights)
    return make_response("Flights Updated", HTTPStatus.OK)


@flights_bp.patch('/<int:id>')
def patch_flights(id: int) -> Response:
    json = request.get_json()
    flights_controller.patch(id, json)
    return make_response("Flights Patched", HTTPStatus.OK)


@flights_bp.delete('/<int:id>')
def delete_flights(id: int) -> Response:
    flights_controller.delete(id)
    return make_response("Flights Deleted", HTTPStatus.OK)

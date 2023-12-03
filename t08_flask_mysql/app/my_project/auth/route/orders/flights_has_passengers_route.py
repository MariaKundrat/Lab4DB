from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import flights_has_passengers_controller
from t08_flask_mysql.app.my_project.auth.domain.orders.flights_has_passengers import FlightHasPassengers

flights_has_passengers_bp = Blueprint('flights_has_passengers', __name__, url_prefix='/flights_has_passengers')


@flights_has_passengers_bp.get('')
def get_all_flights_has_passengers() -> Response:
    return make_response(jsonify(flights_has_passengers_controller.find_all()), HTTPStatus.OK)


@flights_has_passengers_bp.get('/<int:id>')
def get_flights_has_passengers(id: int) -> Response:
    return make_response(jsonify(flights_has_passengers_controller.find_by_id(id)), HTTPStatus.OK)


@flights_has_passengers_bp.post('')
def post_flights_has_passengers() -> Response:
    json = request.get_json()
    flights_has_passengers = FlightHasPassengers.create_from_dto(json)
    flights_has_passengers_controller.create(flights_has_passengers)
    return make_response(jsonify(flights_has_passengers.put_into_dto()), HTTPStatus.OK)


@flights_has_passengers_bp.put('/<int:id>')
def put_flights_has_passengers(id: int) -> Response:
    json = request.get_json()
    order = FlightHasPassengers.create_from_dto(json)
    flights_has_passengers_controller.update(id, order)
    return make_response("Flights Has Passengers Updated", HTTPStatus.OK)


@flights_has_passengers_bp.patch('/<int:id>')
def patch_flights_has_passengers(id: int) -> Response:
    json = request.get_json()
    flights_has_passengers_controller.patch(id, json)
    return make_response("Flights Has Passengers Patched", HTTPStatus.OK)


@flights_has_passengers_bp.delete('/<int:order_id>')
def delete_flights_has_passengers(id: int) -> Response:
    flights_has_passengers_controller.delete(id)
    return make_response("Flights Has Passengers Deleted", HTTPStatus.OK)

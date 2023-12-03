from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import airline_companies_controller
from t08_flask_mysql.app.my_project.auth.domain.orders.airline_companies import AirlineCompanies

airline_companies_bp = Blueprint('airline_companies_connect', __name__, url_prefix='/airline_companies_connect')


@airline_companies_bp.get('')
def get_all_airline_companies_connect() -> Response:
    return make_response(jsonify(airline_companies_controller.find_all()), HTTPStatus.OK)


@airline_companies_bp.get('/<int:id>')
def get_airline_companies_connect(id: int) -> Response:
    return make_response(jsonify(airline_companies_controller.find_by_id(id)),
                         HTTPStatus.OK)


@airline_companies_bp.post('')
def post_airline_companies_connect() -> Response:
    json = request.get_json()
    airline_companies = AirlineCompanies.create_from_dto(json)
    airline_companies_controller.create(airline_companies)
    return make_response(jsonify(airline_companies.put_into_dto()), HTTPStatus.OK)


@airline_companies_bp.put('/<int:id>')
def put_airline_companies_connect(id: int) -> Response:
    json = request.get_json()
    order = AirlineCompanies.create_from_dto(json)
    airline_companies_controller.update(id, order)
    return make_response("Airline Companies Updated", HTTPStatus.OK)


@airline_companies_bp.patch('/<int:id>')
def patch_airline_companies_connect(id: int) -> Response:
    json = request.get_json()
    airline_companies_controller.patch(id, json)
    return make_response("Airline Companies Patched", HTTPStatus.OK)


@airline_companies_bp.delete('/<int:id>')
def delete_airline_companies_connect(id: int) -> Response:
    airline_companies_controller.delete(id)
    return make_response("Airline Companies Deleted", HTTPStatus.OK)

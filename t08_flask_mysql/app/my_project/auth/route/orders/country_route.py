from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import country_controller
from t08_flask_mysql.app.my_project.auth.domain.orders.country import Country

country_bp = Blueprint('country', __name__, url_prefix='/country')


@country_bp.get('')
def get_all_countries() -> Response:
    return make_response(jsonify(country_controller.find_all()), HTTPStatus.OK)


@country_bp.get('/<int:id>')
def get_country(id: int) -> Response:
    return make_response(jsonify(country_controller.find_by_id(id)), HTTPStatus.OK)


@country_bp.post('')
def post_event() -> Response:
    json = request.get_json()
    country = Country.create_from_dto(json)
    country_controller.create(country)
    return make_response(jsonify(country.put_into_dto()), HTTPStatus.OK)


@country_bp.put('/<int:id>')
def put_country(id: int) -> Response:
    json = request.get_json()
    country = Country.create_from_dto(json)
    country_controller.update(id, country)
    return make_response("Country Updated", HTTPStatus.OK)


@country_bp.patch('/<int:id>')
def patch_country(id: int) -> Response:
    json = request.get_json()
    country_controller.patch(id, json)
    return make_response("Country Patched", HTTPStatus.OK)


@country_bp.delete('/<int:id>')
def delete_event(id: int) -> Response:
    country_controller.delete(id)
    return make_response("Country Deleted", HTTPStatus.OK)

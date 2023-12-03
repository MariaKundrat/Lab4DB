from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import city_controller
from t08_flask_mysql.app.my_project.auth.domain.orders.city import City

city_bp = Blueprint('city', __name__, url_prefix='/city')


@city_bp.get('')
def get_all_cities() -> Response:
    return make_response(jsonify(city_controller.find_all()), HTTPStatus.OK)


@city_bp.get('/<int:id>')
def get_city(id: int) -> Response:
    return make_response(jsonify(city_controller.find_by_id(id)), HTTPStatus.OK)


@city_bp.post('')
def post_city() -> Response:
    json = request.get_json()
    city = City.create_from_dto(json)
    city_controller.create(city)
    return make_response(jsonify(city.put_into_dto()), HTTPStatus.OK)


@city_bp.put('/<int:id>')
def put_city(id: int) -> Response:
    json = request.get_json()
    city = City.create_from_dto(json)
    city_controller.update(id, city)
    return make_response("City Updated", HTTPStatus.OK)


@city_bp.patch('/<int:id>')
def patch_city(id: int) -> Response:
    json = request.get_json()
    city_controller.patch(id, json)
    return make_response("City Patched", HTTPStatus.OK)


@city_bp.delete('/<int:id>')
def delete_city(id: int) -> Response:
    city_controller.delete(id)
    return make_response("City Deleted", HTTPStatus.OK)

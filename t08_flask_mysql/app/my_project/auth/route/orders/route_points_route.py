from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import route_points_controller
from t08_flask_mysql.app.my_project.auth.domain.orders.route_points import RoutePoints

route_points_bp = Blueprint('route_points', __name__, url_prefix='/route_points')


@route_points_bp.get('')
def get_all_route_points() -> Response:
    return make_response(jsonify(route_points_controller.find_all()), HTTPStatus.OK)


@route_points_bp.get('/<int:id>')
def get_route_points(id: int) -> Response:
    return make_response(jsonify(route_points_controller.find_by_id(id)), HTTPStatus.OK)


@route_points_bp.post('')
def post_route_points() -> Response:
    json = request.get_json()
    route_points = RoutePoints.create_from_dto(json)
    route_points_controller.create(route_points)
    return make_response(jsonify(route_points.put_into_dto()), HTTPStatus.OK)


@route_points_bp.put('/<int:id>')
def put_route_points(id: int) -> Response:
    json = request.get_json()
    route_points = RoutePoints.create_from_dto(json)
    route_points_controller.update(id, route_points)
    return make_response("Route Points Updated", HTTPStatus.OK)


@route_points_bp.patch('/<int:id>')
def patch_route_points(id: int) -> Response:
    json = request.get_json()
    route_points_controller.patch(id, json)
    return make_response("Route Points Patched", HTTPStatus.OK)


@route_points_bp.delete('/<int:id>')
def delete_route_points(id: int) -> Response:
    route_points_controller.delete(id)
    return make_response("Route Points Deleted", HTTPStatus.OK)

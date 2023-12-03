from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import plane_controller
from t08_flask_mysql.app.my_project.auth.domain.orders.plane import Plane

plane_bp = Blueprint('plane', __name__, url_prefix='/plane')


@plane_bp.get('')
def get_all_planes() -> Response:
    return make_response(jsonify(plane_controller.find_all()), HTTPStatus.OK)


@plane_bp.get('/<int:id>')
def get_plane(id: int) -> Response:
    return make_response(jsonify(plane_controller.find_by_id(id)), HTTPStatus.OK)


@plane_bp.post('')
def post_plane() -> Response:
    json = request.get_json()
    plane = Plane.create_from_dto(json)
    plane_controller.create(plane)
    return make_response(jsonify(plane.put_into_dto()), HTTPStatus.OK)


@plane_bp.put('/<int:id>')
def put_seat(id: int) -> Response:
    json = request.get_json()
    plane = Plane.create_from_dto(json)
    plane_controller.update(id, plane)
    return make_response("Plane Updated", HTTPStatus.OK)


@plane_bp.patch('/<int:id>')
def patch_plane(id: int) -> Response:
    json = request.get_json()
    plane_controller.patch(id, json)
    return make_response("Plane Patched", HTTPStatus.OK)


@plane_bp.delete('/<int:id>')
def delete_plane(id: int) -> Response:
    plane_controller.delete(id)
    return make_response("Plane Deleted", HTTPStatus.OK)

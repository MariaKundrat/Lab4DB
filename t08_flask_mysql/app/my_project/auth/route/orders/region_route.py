from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import region_controller
from t08_flask_mysql.app.my_project.auth.domain.orders.region import Region

region_bp = Blueprint('region', __name__, url_prefix='/region')


@region_bp.get('')
def get_all_regions() -> Response:
    return make_response(jsonify(region_controller.find_all()), HTTPStatus.OK)


@region_bp.get('/<int:id>')
def get_region(id: int) -> Response:
    return make_response(jsonify(region_controller.find_by_id(id)), HTTPStatus.OK)


@region_bp.post('')
def post_region() -> Response:
    json = request.get_json()
    region = Region.create_from_dto(json)
    region_controller.create(region)
    return make_response(jsonify(region.put_into_dto()), HTTPStatus.OK)


@region_bp.put('/<int:id>')
def put_region(id: int) -> Response:
    json = request.get_json()
    region = Region.create_from_dto(json)
    region_controller.update(id, region)
    return make_response("Region Updated", HTTPStatus.OK)


@region_bp.patch('/<int:id>')
def patch_region(id: int) -> Response:
    json = request.get_json()
    region_controller.patch(id, json)
    return make_response("Region Patched", HTTPStatus.OK)


@region_bp.delete('/<int:id>')
def delete_region(id: int) -> Response:
    region_controller.delete(id)
    return make_response("Region Deleted", HTTPStatus.OK)

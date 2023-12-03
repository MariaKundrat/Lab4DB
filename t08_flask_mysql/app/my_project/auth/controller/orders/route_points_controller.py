from t08_flask_mysql.app.my_project.auth.service import route_points_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class RoutePointsController(GeneralController):
    _service = route_points_service

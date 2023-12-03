from t08_flask_mysql.app.my_project.auth.dao import route_points_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class RoutePointsConnectService(GeneralService):
    _dao = route_points_dao

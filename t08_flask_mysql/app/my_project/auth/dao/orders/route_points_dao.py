from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain.orders.route_points import RoutePoints


class RoutePointsDao(GeneralDAO):
    _domain_type = RoutePoints

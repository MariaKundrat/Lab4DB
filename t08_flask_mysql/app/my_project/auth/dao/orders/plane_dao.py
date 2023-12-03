from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain.orders.plane import Plane


class PlaneDao(GeneralDAO):
    _domain_type = Plane

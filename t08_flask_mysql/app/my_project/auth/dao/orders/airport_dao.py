from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class AirportDao(GeneralDAO):
    _domain_type = GeneralController

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain.orders.flight import Flight


class FlightsDao(GeneralDAO):
    _domain_type = Flight

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain.orders.airline_companies import AirlineCompanies


class AirlineCompaniesDao(GeneralDAO):
    _domain_type = AirlineCompanies

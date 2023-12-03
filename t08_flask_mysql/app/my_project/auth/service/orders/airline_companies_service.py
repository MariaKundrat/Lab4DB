from t08_flask_mysql.app.my_project.auth.dao import airline_companies_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class AirlineCompaniesConnectService(GeneralService):
    _dao = airline_companies_dao

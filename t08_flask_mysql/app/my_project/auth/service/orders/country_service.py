from t08_flask_mysql.app.my_project.auth.dao import country_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class CountryConnectService(GeneralService):
    _dao = country_dao

from t08_flask_mysql.app.my_project.auth.dao import city_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class CityConnectService(GeneralService):
    _dao = city_dao

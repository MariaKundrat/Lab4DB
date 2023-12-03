from t08_flask_mysql.app.my_project.auth.dao import flights_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class FlightsConnectService(GeneralService):
    _dao = flights_dao

from t08_flask_mysql.app.my_project.auth.dao import passengers_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class PassengersConnectService(GeneralService):
    _dao = passengers_dao

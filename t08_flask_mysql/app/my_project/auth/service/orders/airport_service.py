from t08_flask_mysql.app.my_project.auth.dao import airport_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class AirportConnectService(GeneralService):
    _dao = airport_dao

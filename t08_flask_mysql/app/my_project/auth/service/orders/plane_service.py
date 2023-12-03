from t08_flask_mysql.app.my_project.auth.dao import plane_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class PlaneConnectService(GeneralService):
    _dao = plane_dao

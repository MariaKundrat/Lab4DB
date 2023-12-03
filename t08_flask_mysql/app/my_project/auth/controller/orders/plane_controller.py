from t08_flask_mysql.app.my_project.auth.service import plane_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class PlaneController(GeneralController):
    _service = plane_service

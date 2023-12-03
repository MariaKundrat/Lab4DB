from t08_flask_mysql.app.my_project.auth.service import passengers_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class PassengersController(GeneralController):
    _service = passengers_service

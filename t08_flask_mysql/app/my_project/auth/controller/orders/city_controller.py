from t08_flask_mysql.app.my_project.auth.service import city_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class CityController(GeneralController):
    _service = city_service

from t08_flask_mysql.app.my_project.auth.service import flights_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class FlightsController(GeneralController):
    _service = flights_service

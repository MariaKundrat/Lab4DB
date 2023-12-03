from t08_flask_mysql.app.my_project.auth.service import flights_has_passengers_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class FlightsHasPassengersController(GeneralController):
    _service = flights_has_passengers_service

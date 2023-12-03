from t08_flask_mysql.app.my_project.auth.service import country_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class CountryController(GeneralController):
    _service = country_service

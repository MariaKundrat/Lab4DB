from t08_flask_mysql.app.my_project.auth.service import airline_companies_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class AirlineCompaniesController(GeneralController):
    _service = airline_companies_service

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain.orders.flights_has_passengers import FlightHasPassengers


class FlightsHasPassengersDao(GeneralDAO):
    _domain_type = FlightHasPassengers

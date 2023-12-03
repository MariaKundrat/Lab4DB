from .orders.airline_companies_controller import AirlineCompaniesController
from .orders.airport_controller import AirportController
from .orders.city_controller import CityController
from .orders.country_controller import CountryController
from .orders.flights_controller import FlightsController
from .orders.flights_has_passengers_controller import FlightsHasPassengersController
from .orders.passengers_controller import PassengersController
from .orders.plane_controller import PlaneController
from .orders.region_controller import RegionController
from .orders.route_points_controller import RoutePointsController

airline_companies_controller = AirlineCompaniesController()
airport_controller = AirportController()
city_controller = CityController()
country_controller = CountryController()
flights_controller = FlightsController()
flights_has_passengers_controller = FlightsHasPassengersController()
passengers_controller = PassengersController()
plane_controller = PlaneController()
region_controller = RegionController()
route_points_controller = RoutePointsController()

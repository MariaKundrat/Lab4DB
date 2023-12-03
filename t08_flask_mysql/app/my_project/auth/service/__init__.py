from .orders.airline_companies_service import AirlineCompaniesConnectService
from .orders.airport_service import AirportConnectService
from .orders.city_service import CityConnectService
from .orders.country_service import CountryConnectService
from .orders.flights_service import FlightsConnectService
from .orders.flights_has_passengers_service import FlightsHasPassengersConnectService
from .orders.passengers_service import PassengersConnectService
from .orders.plane_service import PlaneConnectService
from .orders.region_service import RegionConnectService
from .orders.route_points_service import RoutePointsConnectService

airline_companies_service = AirlineCompaniesConnectService()
airport_service = AirportConnectService()
city_service = CityConnectService()
country_service = CountryConnectService()
flights_service = FlightsConnectService()
flights_has_passengers_service = FlightsHasPassengersConnectService()
passengers_service = PassengersConnectService()
plane_service = PlaneConnectService()
region_service = RegionConnectService()
route_points_service = RoutePointsConnectService()

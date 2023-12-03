from .orders.airline_companies_dao import AirlineCompaniesDao
from .orders.airport_dao import AirportDao
from .orders.city_dao import CityDao
from .orders.country_dao import CountryDao
from .orders.flights_dao import FlightsDao
from .orders.flights_has_passengers_dao import FlightsHasPassengersDao
from .orders.passengers_dao import PassengersDao
from .orders.plane_dao import PlaneDao
from .orders.region_dao import RegionDao
from .orders.route_points_dao import RoutePointsDao

airline_companies_dao = AirlineCompaniesDao()
airport_dao = AirportDao()
city_dao = CityDao()
country_dao = CountryDao()
flights_dao = FlightsDao()
flights_has_passengers_dao = FlightsHasPassengersDao()
passengers_dao = PassengersDao()
plane_dao = PlaneDao()
region_dao = RegionDao()
route_points_dao = RoutePointsDao()

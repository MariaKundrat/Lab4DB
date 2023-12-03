from flask import Flask

from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:
    """
    Registers all necessary Blueprint routes
    :param app: Flask application object
    """
    from .orders.airline_companies_route import airline_companies_bp
    from .orders.airport_route import airport_bp
    from .orders.city_route import city_bp
    from .orders.country_route import country_bp
    from .orders.flights_route import flights_bp
    from .orders.flights_has_passengers_route import flights_has_passengers_bp
    from .orders.passengers_route import passengers_bp
    from .orders.plane_route import plane_bp
    from .orders.region_route import region_bp
    from .orders.route_points_route import route_points_bp

    app.register_blueprint(airline_companies_bp)
    app.register_blueprint(airport_bp)
    app.register_blueprint(city_bp)
    app.register_blueprint(country_bp)
    app.register_blueprint(flights_bp)
    app.register_blueprint(flights_has_passengers_bp)
    app.register_blueprint(passengers_bp)
    app.register_blueprint(plane_bp)
    app.register_blueprint(region_bp)
    app.register_blueprint(route_points_bp)
    app.register_blueprint(err_handler_bp)

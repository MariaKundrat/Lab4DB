from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Flight(db.Model, IDto):
    __tablename__ = "flights"

    id = db.Column(db.Integer, primary_key=True)
    departure_datetime = db.Column(db.DateTime, nullable=False)
    arriving_datetime = db.Column(db.DateTime, nullable=False)
    airport_from = db.Column(db.String(45), nullable=False)
    airport_to = db.Column(db.String(45), nullable=False)
    flight_number = db.Column(db.String(45), nullable=False)
    distance = db.Column(db.DECIMAL)

    plane_id = db.Column(db.Integer, db.ForeignKey('plane.id'), nullable=False)
    route_points_id = db.Column(db.Integer, db.ForeignKey('route_points.id'), nullable=False)

    plane = db.relationship('Plane', backref='flights')
    route_points = db.relationship('RoutePoints', backref='flights')

    def __repr__(self):
        return f"Flight(id={self.id}, flight_number='{self.flight_number}', airport_from='{self.airport_from}', airport_to='{self.airport_to}')"

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, object]) -> Flight:
        obj = Flight(
            departure_datetime=dto_dict.get("departure_datetime"),
            arriving_datetime=dto_dict.get("arriving_datetime"),
            airport_from=dto_dict.get("airport_from"),
            airport_to=dto_dict.get("airport_to"),
            flight_number=dto_dict.get("flight_number"),
            distance=dto_dict.get("distance"),
            plane_id=dto_dict.get("plane_id"),
            route_points_id=dto_dict.get("route_points_id")
        )
        return obj

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "departure_datetime": self.departure_datetime,
            "arriving_datetime": self.arriving_datetime,
            "airport_from": self.airport_from,
            "airport_to": self.airport_to,
            "flight_number": self.flight_number,
            "distance": self.distance,
            "plane_id": self.plane_id,
            "route_points_id": self.route_points_id
        }


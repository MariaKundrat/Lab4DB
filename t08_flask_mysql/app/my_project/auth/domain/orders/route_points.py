from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db


class RoutePoints(db.Model):
    __tablename__ = "route_points"

    id = db.Column(db.Integer, primary_key=True)
    flight_id = db.Column(db.Integer, db.ForeignKey('flight.id'), nullable=True)
    datetime = db.Column(db.DateTime, nullable=True)
    longitude_latitude = db.Column(db.String(45), nullable=True)
    altitude = db.Column(db.DateTime, nullable=True)
    current_speed = db.Column(db.DECIMAL, nullable=True)

    def __repr__(self):
        return f"RoutePoints({self.id}, {self.flight_id}, {self.datetime}, {self.longitude_latitude}, {self.altitude}, {self.current_speed})"

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, object]) -> RoutePoints:
        obj = RoutePoints(
            id=dto_dict.get("id"),
            flight_id=dto_dict.get("flight_id"),
            datetime=dto_dict.get("datetime"),
            longitude_latitude=dto_dict.get("longitude_latitude"),
            altitude=dto_dict.get("altitude"),
            current_speed=dto_dict.get("current_speed")
        )
        return obj

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "flight_id": self.flight_id,
            "datetime": self.datetime,
            "longitude_latitude": self.longitude_latitude,
            "altitude": self.altitude,
            "current_speed": self.current_speed
        }

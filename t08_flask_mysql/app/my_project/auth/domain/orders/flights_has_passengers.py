from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class FlightHasPassengers(db.Model, IDto):
    __tablename__ = "flight_has_passengers"

    flight_id = db.Column(db.Integer, db.ForeignKey('flight.id'), primary_key=True)
    passengers_id = db.Column(db.Integer, db.ForeignKey('passengers.id'), primary_key=True)

    flight = db.relationship('Flight', backref='passengers', foreign_keys=[flight_id])
    passengers = db.relationship('Passengers', backref='flight', foreign_keys=[passengers_id])

    def __repr__(self):
        return f"FlightHasPassengers(flight_id={self.flight_id}, passengers_id={self.passengers_id})"

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, object]) -> FlightHasPassengers:
        obj = FlightHasPassengers(
            flight_id=dto_dict.get("flight_id"),
            passengers_id=dto_dict.get("passengers_id")
        )
        return obj

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "flight_id": self.flight_id,
            "passengers_id": self.passengers_id
        }

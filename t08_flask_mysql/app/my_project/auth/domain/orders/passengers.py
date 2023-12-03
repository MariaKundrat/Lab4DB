from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Passengers(db.Model, IDto):
    __tablename__ = "passengers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    surname = db.Column(db.String(45), nullable=False)
    passport_data = db.Column(db.String(45), nullable=False)
    serial_passport_number = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Passenger(id={self.id}, name='{self.name}', surname='{self.surname}', passport_data='{self.passport_data}', serial_passport_number={self.serial_passport_number})"

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, object]) -> Passengers:
        obj = Passengers(
            name=dto_dict.get("name"),
            surname=dto_dict.get("surname"),
            passport_data=dto_dict.get("passport_data"),
            serial_passport_number=dto_dict.get("serial_passport_number")
        )
        return obj

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "surname": self.surname,
            "passport_data": self.passport_data,
            "serial_passport_number": self.serial_passport_number
        }

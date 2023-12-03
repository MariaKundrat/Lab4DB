from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Airport(db.Model, IDto):
    __tablename__ = "airport"

    id = db.Column(db.Integer, primary_key=True)
    name_index = db.Column(db.String(45), nullable=False)
    code = db.Column(db.String(45), nullable=False)
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'), nullable=False)

    city = db.relationship('City')

    def __repr__(self):
        return f"Airport({self.id}, `{self.name_index}`, `{self.code}`, `{self.city_id}`)"

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, object]) -> Airport:
        obj = Airport(
            name_index=dto_dict.get("name_index"),
            code=dto_dict.get("code"),
            city_id=dto_dict.get("city_id")
        )
        return obj

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name_index": self.name_index,
            "code": self.code,
            "city_id": self.city_id
        }

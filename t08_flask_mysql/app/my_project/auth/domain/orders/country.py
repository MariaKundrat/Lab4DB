from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Country(db.Model, IDto):
    __tablename__ = "country"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)

    def __repr__(self):
        return f"Country(id={self.id}, name='{self.name}')"

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, object]) -> Country:
        obj = Country(
            name=dto_dict.get("name")
        )
        return obj

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name
        }

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class City(db.Model, IDto):
    __tablename__ = "city"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    region_id = db.Column(db.Integer, db.ForeignKey('region.id'), nullable=False)

    region = db.relationship('Region', backref='cities')

    def __repr__(self):
        return f"City(id={self.id}, name='{self.name}', region_id={self.region_id})"

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, object]) -> City:
        obj = City(
            name=dto_dict.get("name"),
            region_id=dto_dict.get("region_id")
        )
        return obj

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "region_id": self.region_id,
            "region": {
                "id": self.region.id,
                "name": self.region.name
            }
        }

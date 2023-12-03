from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Region(db.Model, IDto):
    __tablename__ = "region"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    country_id = db.Column(db.Integer, nullable=False)

    __table_args__ = (
        db.PrimaryKeyConstraint('id', 'id'),
        db.Index('fk_region_country1_idx', 'id'),
        db.ForeignKeyConstraint(['country_id'], ['country.id'],
                                name='fk_region_country2', ondelete='NO ACTION', onupdate='NO ACTION')
    )

    def __repr__(self):
        return f"Region({self.id}, {self.name}, {self.country_id})"

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, object]) -> Region:
        obj = Region(
            id=dto_dict.get("id"),
            name=dto_dict.get("name"),
            country_id=dto_dict.get("country_id")
        )
        return obj

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "country_id": self.country_id
        }

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Plane(db.Model, IDto):
    __tablename__ = "plane"

    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(45), nullable=True)
    total_flight_hours = db.Column(db.DECIMAL, nullable=True)
    serial_number = db.Column(db.Integer, nullable=False)
    airline_company_id = db.Column(db.Integer, nullable=False)

    __table_args__ = (
        db.PrimaryKeyConstraint('id', 'id'),
        db.Index('number', 'serial_number'),
        db.Index('fk_plane_airline_company1_idx', 'id'),
        db.ForeignKeyConstraint(['airline_company_id'], ['airline_company.id'],
                                name='fk_plane_airline_company1', ondelete='NO ACTION', onupdate='NO ACTION')
    )

    def __repr__(self):
        return f"Plane({self.id}, {self.model}, {self.total_flight_hours}, {self.serial_number}, {self.airline_company_id})"

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, object]) -> Plane:
        obj = Plane(
            id=dto_dict.get("id"),
            model=dto_dict.get("model"),
            total_flight_hours=dto_dict.get("total_flight_hours"),
            serial_number=dto_dict.get("serial_number"),
            airline_company_id=dto_dict.get("airline_company_id")
        )
        return obj

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "model": self.model,
            "total_flight_hours": self.total_flight_hours,
            "serial_number": self.serial_number,
            "airline_company_id": self.airline_company_id
        }

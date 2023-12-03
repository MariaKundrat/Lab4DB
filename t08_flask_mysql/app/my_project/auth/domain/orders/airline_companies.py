from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class AirlineCompanies(db.Model, IDto):
    __tablename__ = "airline_company"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=True)
    city_id = db.Column(db.Integer, nullable=True)
    address_info = db.Column(db.String(45), nullable=True)
    phone_number = db.Column(db.String(45), nullable=True)

    event_airline_company = db.relationship('AirlineCompany', backref="airline_companies")

    def __repr__(self):
        return f"AirlineCompanies({self.id}, `{self.name}`, `{self.city_id}`, `{self.address_info}`, `{self.phone_number}`)"

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, object]) -> AirlineCompanies:
        obj = AirlineCompanies(
            name=dto_dict.get("name"),
            city_id=dto_dict.get("city_id"),
            address_info=dto_dict.get("address_info"),
            phone_number=dto_dict.get("phone_number")
        )
        return obj

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "city_id": self.city_id,
            "address_info": self.adress_info,
            "phone_number": self.phone_number,
            "events": [
                {
                    "idevent": airline_company_event_pair.event.idevent,
                    "eventname": airline_company_event_pair.event.eventname,
                    "datetime": airline_company_event_pair.event.datetime,
                    "Place":
                        {
                            "idPlaces": airline_company_event_pair.event.place.idPlaces,
                            "addresses": airline_company_event_pair.event.place.addresses,
                            "Place_name": airline_company_event_pair.event.place.Place_name
                        }
                } for airline_company_event_pair in self.event_airline_company]
        }

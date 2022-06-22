from datetime import date
from enum import Enum

from pydantic import BaseModel


class CountryEnum(Enum, int):
    cameroon: int = 237


class OrderInput(BaseModel):
    id: int
    email: str
    phone_number: str
    country: int
    parcel_weight: float


class Order(OrderInput):
    country: int
    date_created: date = None

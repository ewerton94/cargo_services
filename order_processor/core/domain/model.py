from datetime import date

from pydantic import BaseModel


class OrderInput(BaseModel):
    id: int
    email: str
    phone_number: str
    country: int
    parcel_weight: float


class Order(OrderInput):
    country: int
    date_created: date = None

from datetime import date

from pydantic import BaseModel


class OrderInput(BaseModel):
    id: int
    email: str
    phone_number: str
    parcel_weight: float


class Order(OrderInput):
    country: int = None
    date_created: date = None

    class Config:
        orm_mode = True

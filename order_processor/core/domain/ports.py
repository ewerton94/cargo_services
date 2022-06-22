from typing import List, Protocol

from core.domain.model import Order


class CountryFinder(Protocol):

    def find_country_from_phone_number(self, phone_number: str) -> int:
        ...


class OrderProcessor(Protocol):

    def transform_file_in_orders(self, file: str) -> List[Order]:
        ...


class OrderRepository(Protocol):

    def send_order(self, order: Order) -> None:
        ...

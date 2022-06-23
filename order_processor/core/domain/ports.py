from typing import List, Protocol, BinaryIO

from core.domain.model import Order


class CountryFinder(Protocol):

    async def find_country_from_phone_number(self, phone_number: str) -> int:
        ...


class OrderProcessor(Protocol):

    async def transform_file_in_orders(self, file: BinaryIO) -> List[Order]:
        ...


class OrderRepository(Protocol):

    async def send_order(self, order: Order) -> None:
        ...

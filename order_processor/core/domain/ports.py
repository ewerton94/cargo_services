from typing import Protocol, BinaryIO, Generator

from core.domain.model import Order


class CountryFinder(Protocol):

    def find_country_from_phone_number(self, phone_number: str) -> int:
        ...


class OrderProcessor(Protocol):

    async def transform_file_in_orders(self, file: BinaryIO)\
            -> Generator[Order]:
        ...


class OrderRepository(Protocol):

    async def send_order(self, order: Order) -> None:
        ...

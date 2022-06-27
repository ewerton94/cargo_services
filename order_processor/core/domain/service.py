from datetime import date
import multiprocessing as mp
from typing import BinaryIO, Generator

from core.domain.ports import CountryFinder, OrderProcessor, OrderRepository
from core.domain.model import OrderInput, Order


class Service:

    def __init__(
            self,
            country_finder: CountryFinder,
            order_processor: OrderProcessor,
            order_repository: OrderRepository
    ):
        self.country_finder = country_finder
        self.order_processor = order_processor
        self.order_repository = order_repository

    async def order_receiver(self, date_created: date, file: BinaryIO):
        input_orders = await self.order_processor.transform_file_in_orders(
            file
        )
        orders = self.build_orders(input_orders, date_created)
        await self.send_orders(orders)

    def build_orders(
            self,
            input_orders: Generator[OrderInput],
            date_created: date
    ) -> Generator[Order]:
        for order in input_orders:
            order = Order.from_orm(order)
            order.country = self.country_finder.find_country_from_phone_number(
                order.phone_number
            )
            order.date_created = date_created
            yield order

    async def send_orders(self, orders: Generator[Order]):
        """
        Send orders in parallel

        :param orders: Generator[Order]
        :return: None
        """
        pool = mp.Pool(mp.cpu_count())
        pool.imap(self.order_repository.send_order, orders)

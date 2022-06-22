from datetime import date
from typing import List

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

    def build_orders(
            self,
            input_orders: List[OrderInput],
            date_created: date
    ) -> List[Order]:
        for order in input_orders:
            order = Order.from_orm(order)
            order.country = self.country_finder.find_country_from_phone_number(
                order.phone_number
            )
            order.date_created = date_created
            yield order

    def order_receiver(self, date_created: date, file):
        input_orders = self.order_processor.transform_file_in_orders(file)
        orders = self.build_orders(input_orders, date_created)
        self.send_orders(orders)

    def send_orders(self, orders: List[Order]):
        for order in orders:
            self.order_repository.send_order(order)

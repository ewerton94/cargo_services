from typing import List, BinaryIO

from core.domain.model import Order


class OrderProcessorPandas:

    async def transform_file_in_orders(self, file: BinaryIO) -> List[Order]:
        pass

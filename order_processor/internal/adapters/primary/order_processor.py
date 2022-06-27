import io
import codecs

import csv
from typing import BinaryIO, Generator

from core.domain.model import OrderInput


class OrderProcessorPandas:

    @staticmethod
    async def transform_file_in_orders(file: BinaryIO) \
            -> Generator[OrderInput]:
        file = io.BytesIO(file.read().replace(b', ', b','))
        rows = (
            OrderInput.parse_obj(row)
            for row in csv.DictReader(codecs.iterdecode(file, 'utf-8'))
        )
        return rows

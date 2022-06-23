from internal.adapters.primary.order_processor import OrderProcessorPandas
from internal.adapters.primary.country_finder import CountryFinderInMemory
from internal.adapters.secondary.order_api import OrderRepositoryAPI
from core.domain.service import Service


async def build_service():
    order_processor = OrderProcessorPandas()
    country_finder = CountryFinderInMemory()
    order_repository = OrderRepositoryAPI()

    service = Service(country_finder, order_processor, order_repository)

    return service

from fastapi import FastAPI

from .controllers import router


app = FastAPI(
    title='Order Processor Service',
    version='0.1.0',
    openapi_tags=[
        {
            'name': 'order_processor',
            'description': 'Order Processor Service'
        }
    ]
)

app.include_router(
    router, prefix="", tags=['Order processor']
)

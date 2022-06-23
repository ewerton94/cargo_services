from datetime import date

from fastapi import APIRouter, status, UploadFile, File, Depends

from api.dependency_injection import build_service
from core.domain.service import Service

router = APIRouter()


@router.post(
    '/new_file',
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        204: {'model': None}
    }
)
async def send_new_file(
        date_created: date,
        data_file: UploadFile = File(...),
        service: Service = Depends(build_service)
):

    await service.order_receiver(date_created, data_file.file)

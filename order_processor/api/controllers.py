from datetime import date

from fastapi import APIRouter, status, UploadFile, File

router = APIRouter()


@router.post(
    '/new_file',
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        204: {'model': None}
    }
)
async def send_new_file(date_created: date, data_file: UploadFile = File(...)):
    pass

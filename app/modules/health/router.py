from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.database.session import get_db

router = APIRouter()


@router.get("/db")
async def check_database(db: AsyncSession = Depends(get_db)):
    result = await db.execute(text("SELECT 1"))

    return {
        "app": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "database": "connected",
        "result": result.scalar(),
    }


# from app.core.exceptions import AppException


# @router.get("/test-error")
# async def test_error():
#     raise AppException(
#         message="This is a test error",
#         status_code=400,
#     )

from fastapi import APIRouter

from app.core.config import settings
from app.modules.appointments.router import router as appointments_router
from app.modules.doctors.router import router as doctors_router
from app.modules.health.router import router as health_router

router = APIRouter()


@router.get("/")
def root():
    return {
        "app": "Clinova",
        "version": settings.APP_VERSION,
        "message": "Welcome to Clinova!",
    }


router.include_router(
    doctors_router,
    prefix="/doctors",
    tags=["Doctors"],
)

router.include_router(
    appointments_router,
    prefix="/appointments",
    tags=["Appointments"],
)

router.include_router(
    health_router,
    prefix="/health",
    tags=["Health"],
)

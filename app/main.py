from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.router import router
from app.core.config import settings
from app.core.exception_handlers import app_exception_handler
from app.core.exceptions import AppException
from app.database.session import engine


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Clinova is starting...")

    yield

    await engine.dispose()
    print("Clinova is shutting down...")


app = FastAPI(
    title=settings.APP_NAME,
    description="Online Clinic Appointment Booking System",
    version=settings.APP_VERSION,
    debug=settings.DEBUG,
    lifespan=lifespan,
)

app.add_exception_handler(
    AppException,
    app_exception_handler,
)

app.include_router(router)

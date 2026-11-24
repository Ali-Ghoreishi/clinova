from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def list_appointments():
    return {"message": "Appointments list"}
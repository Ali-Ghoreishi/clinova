from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def list_doctors():
    return {"message": "Doctors list"}
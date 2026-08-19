from fastapi import APIRouter

from linux.storage import get_storage_status


router = APIRouter()


@router.get("/storage")
def storage():
    return {
        "success": True,
        "data": get_storage_status()
    }

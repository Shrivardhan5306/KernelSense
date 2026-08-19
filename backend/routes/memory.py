from fastapi import APIRouter

from linux.memory import get_memory_status


router = APIRouter()


@router.get("/memory")
def memory():
    return {
        "success": True,
        "data": get_memory_status()
    }

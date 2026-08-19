from fastapi import APIRouter

from linux.process import get_process_status


router = APIRouter()


@router.get("/processes")
def processes():
    return {
        "success": True,
        "data": get_process_status()
    }

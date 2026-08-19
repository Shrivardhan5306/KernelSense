from fastapi import APIRouter
from linux.cpu import get_cpu_usage

router = APIRouter()


@router.get("/cpu")
def cpu():
    return {
        "success": True,
        "data": {
            "usage_percent": get_cpu_usage()
        }
    }

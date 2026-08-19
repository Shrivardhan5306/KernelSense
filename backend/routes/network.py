from fastapi import APIRouter

from linux.network import get_network_status


router = APIRouter()


@router.get("/network")
def network():
    return {
        "success": True,
        "data": get_network_status()
    }

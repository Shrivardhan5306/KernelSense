from fastapi import APIRouter, Query

from linux.logs import (
    get_recent_logs,
    get_error_logs,
    get_kernel_logs,
    get_service_logs,
    get_log_status
)


router = APIRouter()


@router.get("/logs")
def logs():
    return {
        "success": True,
        "data": get_log_status()
    }


@router.get("/logs/recent")
def recent_logs(
    limit: int = Query(default=50, ge=1, le=500)
):
    return {
        "success": True,
        "data": get_recent_logs(limit)
    }


@router.get("/logs/errors")
def error_logs(
    limit: int = Query(default=50, ge=1, le=500)
):
    return {
        "success": True,
        "data": get_error_logs(limit)
    }


@router.get("/logs/kernel")
def kernel_logs(
    limit: int = Query(default=50, ge=1, le=500)
):
    return {
        "success": True,
        "data": get_kernel_logs(limit)
    }


@router.get("/logs/service")
def service_logs(
    service: str,
    limit: int = Query(default=50, ge=1, le=500)
):
    return {
        "success": True,
        "data": get_service_logs(service, limit)
    }

from fastapi import APIRouter, Query

from linux.files import (
    get_file_info,
    search_files,
    find_large_files,
    get_directory_info
)


router = APIRouter()


@router.get("/files/info")
def file_info(path: str):
    return {
        "success": True,
        "data": get_file_info(path)
    }


@router.get("/files/search")
def file_search(
    directory: str,
    filename: str
):
    return {
        "success": True,
        "data": search_files(directory, filename)
    }


@router.get("/files/large")
def large_files(
    directory: str,
    min_size_mb: int = Query(default=100, ge=1)
):
    return {
        "success": True,
        "data": find_large_files(directory, min_size_mb)
    }


@router.get("/files/directory")
def directory_info(directory: str):
    return {
        "success": True,
        "data": get_directory_info(directory)
    } 

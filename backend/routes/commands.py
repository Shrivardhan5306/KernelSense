from fastapi import APIRouter
from pydantic import BaseModel, Field

from security.executor import execute_command


router = APIRouter()


class CommandRequest(BaseModel):
    command: list[str] = Field(
        min_length=1,
        description="Linux command represented as a list of arguments"
    )


@router.post("/commands/execute")
def execute_linux_command(request: CommandRequest):
    return execute_command(request.command)

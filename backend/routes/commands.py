from fastapi import APIRouter
from pydantic import BaseModel, Field

from security.executor import execute_command
from security.validator import validate_command


router = APIRouter()


class CommandRequest(BaseModel):
    command: list[str] = Field(
        min_length=1,
        description="Linux command represented as a list of arguments"
    )


@router.post("/commands/execute")
def execute_linux_command(request: CommandRequest):

    validation = validate_command(request.command)

    if validation["requires_approval"]:
        return {
            "success": False,
            "command": request.command,
            "risk": validation["risk"],
            "blocked": False,
            "requires_approval": True,
            "reason": validation["reason"]
        }

    if not validation["allowed"]:
        return {
            "success": False,
            "command": request.command,
            "risk": validation["risk"],
            "blocked": True,
            "requires_approval": False,
            "reason": validation["reason"]
        }

    result = execute_command(request.command)

    return {
        **result,
        "risk": validation["risk"],
        "blocked": False,
        "requires_approval": False,
        "validation_reason": validation["reason"]
    }

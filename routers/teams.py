from fastapi import APIRouter

router = APIRouter(
    prefix="/teams",
    tags=["teams"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def list_teams():
    """Get a list of all NBA teams"""
    return {"teams": []}


@router.get("/{team_id}")
async def get_team(team_id: str):
    """Get information about a specific team"""
    return {"team_id": team_id}

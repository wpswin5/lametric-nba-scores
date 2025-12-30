from fastapi import APIRouter

from nba_api.live.nba.endpoints import scoreboard

router = APIRouter(
    prefix="/scores",
    tags=["scores"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def list_scores():
    """Get a list of recent NBA game scores"""

    # Today's Score Board
    board = scoreboard.ScoreBoard()

    # dictionary
    resp = board.games.data

    return resp


@router.get("/{team_code}")
async def get_score(team_code: str):
    """Get the score for a specific game"""
    # Today's Score Board
    board = scoreboard.ScoreBoard()

    # dictionary
    resp = board.games.data

    for game in resp:
        if team_code.upper() in (game['homeTeam']['teamTricode'], game['awayTeam']['teamTricode']):
            # simplified format: status, home vs away : score
            return {
                "status": game['gameStatusText'],
                "home_team": game['homeTeam']['teamTricode'],
                "home_score": game['homeTeam']['score'],
                "away_team": game['awayTeam']['teamTricode'],
                "away_score": game['awayTeam']['score'],
            }
    return {
        "status": "Game not found for team code: {}".format(team_code),
        "home_team": None,
        "home_score": None,
        "away_team": None,
        "away_score": None
    }

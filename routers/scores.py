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

    # base response
    frames = {
        "frames": []
    }

    # return all scores in lametric format
    for game in resp:
        frames["frames"].append(
            {
                "text": "{} vs {}".format(
                    game['homeTeam']['teamTricode'],
                    game['awayTeam']['teamTricode']
                ),
                "icon": 44958  # Placeholder icon ID
            }
        )
        frames["frames"].append(
            {
                "text": "{} {}".format(
                    game['homeTeam']['teamTricode'],
                    game['homeTeam']['score']
                ),
                "icon": 1489  # Placeholder icon ID
            }
        )
        frames["frames"].append(
            {
                "text": "{} {}".format(
                    game['awayTeam']['teamTricode'],
                    game['awayTeam']['score']
                ),
                "icon": 1489  # Placeholder icon ID
            }
        )
        frames["frames"].append(
            {
                "text": game['gameStatusText'],
                "icon": 1489  # Placeholder icon ID
            }
        )

    return frames


@router.get("/{team_code}")
async def get_score(team_code: str):
    """Get the score for a specific game"""
    # Today's Score Board
    board = scoreboard.ScoreBoard()

    # dictionary
    resp = board.games.data

    for game in resp:
        if team_code.upper() in (game['homeTeam']['teamTricode'], game['awayTeam']['teamTricode']):
            # sLaMetric format
            return {
                "frames": [
                    {
                        "text": "{} vs {}".format(
                            game['homeTeam']['teamTricode'],
                            game['awayTeam']['teamTricode']
                        ),
                        "icon": 44958  # Placeholder icon ID
                    },
                    {
                        "text": "{} {}".format(
                            game['homeTeam']['teamTricode'],
                            game['homeTeam']['score']
                        ),
                        "icon": 1489  # Placeholder icon ID
                    },
                                        {
                        "text": "{} {}".format(
                            game['awayTeam']['teamTricode'],
                            game['awayTeam']['score']
                        ),
                        "icon": 1489  # Placeholder icon ID
                    },
                    {
                        "text": game['gameStatusText'],
                        "icon": 1489  # Placeholder icon ID
                    }
                ]
            }

    return {
        "status": "Game not found for team code: {}".format(team_code),
        "home_team": None,
        "home_score": None,
        "away_team": None,
        "away_score": None
    }

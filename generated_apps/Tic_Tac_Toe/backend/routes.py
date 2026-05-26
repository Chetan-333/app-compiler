
from fastapi import APIRouter

router = APIRouter()


@router.post("/games")
def _games():
    return {"message": "Create a new game"}


@router.get("/games")
def _games():
    return {"message": "Get all games"}


@router.get("/games/{game_id}")
def _games_{game_id}():
    return {"message": "Get a game by id"}


@router.get("/games/{game_id}/board")
def _games_{game_id}_board():
    return {"message": "Get the game board"}


@router.patch("/games/{game_id}/board")
def _games_{game_id}_board():
    return {"message": "Update the game board"}


@router.get("/games/{game_id}/score")
def _games_{game_id}_score():
    return {"message": "Get the game score"}


@router.post("/players")
def _players():
    return {"message": "Create a new player"}


@router.get("/players")
def _players():
    return {"message": "Get all players"}


@router.get("/players/{player_id}")
def _players_{player_id}():
    return {"message": "Get a player by id"}


@router.get("/multiplayer/lobby")
def _multiplayer_lobby():
    return {"message": "Get the multiplayer lobby"}


@router.post("/multiplayer/lobby")
def _multiplayer_lobby():
    return {"message": "Join the multiplayer lobby"}


@router.delete("/multiplayer/lobby")
def _multiplayer_lobby():
    return {"message": "Leave the multiplayer lobby"}


@router.get("/scoreboard")
def _scoreboard():
    return {"message": "Get the scoreboard"}


@router.get("/dashboard/player")
def _dashboard_player():
    return {"message": "Get the player dashboard"}


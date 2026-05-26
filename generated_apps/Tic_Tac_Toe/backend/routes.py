
from fastapi import APIRouter

router = APIRouter()


@router.post("/games")
def _games():
    return {"message": "Start a new Tic Tac Toe game"}


@router.get("/games/{game_id}")
def _games_{game_id}():
    return {"message": "Retrieve the current state of a specific Tic Tac Toe game, including the board, current player, and outcome"}


@router.post("/games/{game_id}/moves")
def _games_{game_id}_moves():
    return {"message": "Submit a player's move for a specific Tic Tac Toe game"}


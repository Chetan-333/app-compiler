
from fastapi import APIRouter

router = APIRouter()


@router.post("/game/start")
def _game_start():
    return {"message": "Initializes a new Tic Tac Toe game instance."}


@router.get("/game")
def _game():
    return {"message": "Retrieves the current state of the Tic Tac Toe game, including the board, current player, and game status (ongoing, win, draw)."}


@router.post("/game/move")
def _game_move():
    return {"message": "Submits a player's move to place a mark (X or O) on a specified cell of the game board."}


@router.post("/game/reset")
def _game_reset():
    return {"message": "Resets the current game to its initial empty state, allowing a new game to begin."}


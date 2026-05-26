
from sqlalchemy import Column, Integer, String
from database import Base


class Players(Base):
    __tablename__ = 'players'

    id = Column(Integer)
    username = Column(String)


class Game_boards(Base):
    __tablename__ = 'game_boards'

    id = Column(Integer)
    player1_id = Column(Integer)
    player2_id = Column(Integer)
    board_state = Column(String)


class Scores(Base):
    __tablename__ = 'scores'

    id = Column(Integer)
    player_id = Column(Integer)
    score = Column(Integer)


class Multiplayer_lobbies(Base):
    __tablename__ = 'multiplayer_lobbies'

    id = Column(Integer)
    lobby_name = Column(String)


class Player_lobby_joins(Base):
    __tablename__ = 'player_lobby_joins'

    id = Column(Integer)
    player_id = Column(Integer)
    lobby_id = Column(Integer)


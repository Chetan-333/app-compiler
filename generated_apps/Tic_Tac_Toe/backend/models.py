
from sqlalchemy import Column, Integer, String
from database import Base


class Players(Base):
    __tablename__ = 'players'

    id = Column(Integer)
    username = Column(String)


class Games(Base):
    __tablename__ = 'games'

    id = Column(Integer)
    player_x_id = Column(Integer)
    player_o_id = Column(Integer)
    current_turn_player_id = Column(Integer)
    status = Column(String)
    winner_id = Column(Integer)
    board_state = Column(String)


class Moves(Base):
    __tablename__ = 'moves'

    id = Column(Integer)
    game_id = Column(Integer)
    player_id = Column(Integer)
    position = Column(Integer)
    symbol = Column(String)
    move_number = Column(Integer)


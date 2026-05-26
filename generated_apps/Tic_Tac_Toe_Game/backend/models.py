
from sqlalchemy import Column, Integer, String
from database import Base


class Players(Base):
    __tablename__ = 'players'

    id = Column(Integer)
    username = Column(String)
    created_at = Column(String)
    updated_at = Column(String)


class Games(Base):
    __tablename__ = 'games'

    id = Column(Integer)
    player1_id = Column(Integer)
    player2_id = Column(Integer)
    current_turn_player_id = Column(Integer)
    board_state = Column(String)
    status = Column(String)
    winner_id = Column(Integer)
    created_at = Column(String)
    updated_at = Column(String)


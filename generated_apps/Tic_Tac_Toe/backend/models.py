
from sqlalchemy import Column, Integer, String
from database import Base


class Players(Base):
    __tablename__ = 'players'

    id = Column(Integer)
    name = Column(String)
    created_at = Column(String)


class Games(Base):
    __tablename__ = 'games'

    id = Column(Integer)
    player_x_id = Column(Integer)
    player_o_id = Column(Integer)
    current_player_id = Column(Integer)
    board_state = Column(String)
    status = Column(String)
    started_at = Column(String)
    finished_at = Column(String)


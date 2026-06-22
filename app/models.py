from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Float

Base = declarative_base()

class Trade(Base):
    __tablename__ = "trades"

    id = Column(Integer, primary_key=True, autoincrement=True)

    ticket = Column(Integer, unique=True)  # Unique identifier from the trading platform

    symbol = Column(String)          # EURUSD, GBPUSD, etc.

    direction = Column(String)       # BUY or SELL

    open_time = Column(String)
    close_time = Column(String)

    volume = Column(Float)

    open_price = Column(Float)
    close_price = Column(Float)

    profit = Column(Float)

    commission = Column(Float)

    swap = Column(Float)

    strategy = Column(String, nullable=True)
    setup = Column(String, nullable=True)
    emotion = Column(String, nullable=True)
    notes = Column(String, nullable=True)
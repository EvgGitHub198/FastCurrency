from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from app.db import Base


class ConversionHistory(Base):
    __tablename__ = "conversion_history"

    id = Column(Integer, primary_key=True, index=True)
    from_currency = Column(String, index=True)
    to_currency = Column(String, index=True)
    value = Column(Float)
    result = Column(Float)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())




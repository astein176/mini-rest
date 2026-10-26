from datetime import datetime

from sqlalchemy import DateTime, Float, String
from sqlalchemy.orm import Mapped, mapped_column

from database import Base

class BlipRecord(Base):
    __tablename__ = "blips"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    flight_id: Mapped[str] = mapped_column(String(8), index=True)
    latitude: Mapped[float] = mapped_column(Float)
    longitude: Mapped[float] = mapped_column(Float)
    altitude: Mapped[float] = mapped_column(Float)
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True))
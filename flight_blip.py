from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field

class FlightBlip(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    flight_id: str = Field(min_length=2, max_length=8, pattern=r"^[A-Z0-9]+$")
    latitude: float = Field(..., ge=-90, le=90)
    longitude: float = Field(..., ge=-180, le=180)
    altitude: float = Field(..., ge=0, le=100000)  # Altitude in feet
    timestamp: datetime
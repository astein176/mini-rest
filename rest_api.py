from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Path
from flight_blip import FlightBlip

from sqlalchemy import select
from sqlalchemy.orm import Session
from database import Base, ENGINE, get_db
from models import BlipRecord

app = FastAPI()

Base.metadata.create_all(bind=ENGINE)

@app.post("/v0/blips", status_code=201)
def create_blip(blip: FlightBlip, db: Session = Depends(get_db)):
    record = BlipRecord(**blip.model_dump())
    db.add(record)
    db.commit()
    db.refresh(record)
    return record


@app.get("/v0/blips/{blip_id}")
def get_blip(
    blip_id: Annotated[int, Path(ge=1, le=2_147_483_647)],
    db: Session = Depends(get_db),
):
    record = db.scalars(
        select(BlipRecord)
        .where(BlipRecord.id == blip_id)
        .order_by(BlipRecord.id)
    ).first()

    if record is None:
        raise HTTPException(status_code=404, detail="Blip not found")
    return record


@app.get("/v0/blips")
def list_blips(db: Session = Depends(get_db)):
    return db.scalars(
        select(BlipRecord).order_by(BlipRecord.id)
    ).all()

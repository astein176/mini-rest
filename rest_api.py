from fastapi import FastAPI, HTTPException
from flight_blip import FlightBlip

app = FastAPI()
blips = {}
next_id = 1

@app.post("/v0/blips", status_code=201)
def create_blip(blip: FlightBlip):
    global next_id
    blips[next_id] = {"id": next_id, **blip.model_dump()}
    next_id += 1
    return blip

@app.get("/v0/blips/{blip_id}")
def get_blip(blip_id: str):
    for counter_entry in blips.values():
        if blip_id == counter_entry["flight_id"]:
            return counter_entry
    
    raise HTTPException(status_code=404, detail="Blip not found")

@app.get("/v0/debug")
def debug():
    return blips

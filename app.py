from fastapi import FastAPI, HTTPException, Response
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, ValidationError
from uuid import UUID,uuid4

class Tank(BaseModel):
	id: UUID = Field(default_factory=uuid4)
	location: str
	lat: float
	long: float
	
	
class Tank_Update(BaseModel):
	location: str | None = None
	lat: float | None = None
	long: float | None = None
	
app = FastAPI()

tanks = []

@app.get("/tank")
async def get_tanks():
	return tanks

@app.get("/tank/{id}")
async def get_single_tank(id: UUID):
    for element in tanks:
        if element.id == id:
            temp_json = jsonable_encoder(element)	
            return JSONResponse(temp_json, status_code = 200)
    raise HTTPException (status_code = 404, detail = "No Tank found with that ID")

@app.post("/tank")
async def new_tank(new_tank: Tank):
    tanks.append(new_tank)

    tanks_json = jsonable_encoder(new_tank)

    return JSONResponse(tanks_json, status_code=200)

@app.delete("/tank/{id}")
async def remove_tanks(id:UUID):
    for i, tank in enumerate(tanks):
        if tank.id == id:
            del tanks[i]
            return Response(status_code=204, content = "This tank has been deleted")
    raise HTTPException(status_code=404, detail="Tank not found")

@app.patch("/tank/{id}")
async def update_tank(id:UUID, tank_update: Tank_Update):
    for i, tank in enumerate(tanks):
        if tank.id == id:
             tank_update_dict = tank_update.model_dump(exclude_unset = True)

             try:
                  updated_tank = tank.model_copy(update=tank_update_dict)
                  tanks[i] = tank.model_validate(updated_tank)
                  json_updated_tank = jsonable_encoder(tank)
                  return JSONResponse(json_updated_tank, status_code = 200)
             except ValidationError:
                  raise HTTPException(status_code=400, detail="Tank update has wrong type")
        raise HTTPException(status_code=404, detail="Tank does not exist")
                  


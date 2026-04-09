from fastapi import APIRouter, Query
from app.services.place_service import PlaceService

router = APIRouter()

@router.get("/",description="Get a list of places limited by parameter")
def get_places(limit: int = Query(5,description="Limit of places to list")):
    return PlaceService.get_places(limit)
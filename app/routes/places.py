from fastapi import APIRouter, Query
from app.services.place_service import PlaceService

router = APIRouter()

@router.get("/",description="Get a list of places")
def get_places(limit: int = Query(10,description="Limit of places to list"),
               offset: int = Query(0,description="Offset of places to list"),  
               province:str = Query(None,description="province of the places to filter"),
               city:str = Query(None,description="city of the places to filter"),
               keywords: str = Query(None,description="keywords to find a place"),
               latitude: float = Query(None,description="latitude to find nearby places"),
               longitude: float = Query(None,description="longitude to find nearby places"), 
               radius: float = Query(10,description="radius to find nearby places")):
    return PlaceService.get_places(limit,province,city,keywords,latitude,longitude,radius)
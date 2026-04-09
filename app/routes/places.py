from fastapi import APIRouter, Query
from app.services.place_service import PlaceService

router = APIRouter()

@router.get("/",description="Get a list of places limited by parameter")
def get_places(limit: int = Query(5,description="Limit of places to list")):
    return PlaceService.get_places(limit)

@router.get("/filter",description="Get a list of places associated to the province and city passed by parameter")
def get_places(province:str = Query(None,description="province"),
               city:str = Query(None,description="city")  

):
    return PlaceService.filter_places(province,city)

@router.get("/search",description="Get a list of places that contain the words passed by parameter")
def search_places(query: str = Query(None,description="query")):
    return PlaceService.search_places(query)
from fastapi import APIRouter, Query, Depends
from fastapi.responses import JSONResponse
from app.services.place_service import PlaceService
from dependencies import get_place_service

router = APIRouter()

@router.get("/",description="Get a list of places")
def get_places(limit: int = Query(10,ge=1,le=100,description="Limit of places to list"),
               offset: int = Query(0,ge=0,description="Offset of places to list"),  
               province:str = Query(None,description="province of the places to filter"),
               city:str = Query(None,description="city of the places to filter"),
               keywords: str = Query(None,description="keywords to find a place"),
               latitude: float = Query(None,ge=-90,le=90,description="latitude to find nearby places"),
               longitude: float = Query(None,ge=-180,le=180,description="longitude to find nearby places"), 
               radius: float = Query(None,ge=0,le=1000,description="radius to find nearby places"),
               place_service: PlaceService = Depends(get_place_service)
               ):

    # parameters validation			   
    if radius is not None and (latitude is None or longitude is None):
        return JSONResponse(
            status_code = 400,
            content = {
                "success": False,
                "error": {
                    "code": "INVALID_PARAMS",
                    "message": "latitude and longitude are required when using radius"                    					
                }				
            }
        )

    if (latitude is not None and longitude is None) or (longitude is not None and latitude is None):
        return JSONResponse(
            status_code = 400,
            content = {
                "success": False,
                "error": {
                    "code": "INVALID_PARAMS",
                    "message": "both latitude and longitude must be provided together"                    					
                }				
            }        
        )        
    
    return place_service.get_places(limit,offset,province,city,keywords,latitude,longitude,radius)
from fastapi import Depends
from app.repositories.csv_repository import CSVRepository
from app.services.place_service import PlaceService

def get_place_service()-> PlaceService:
    repo = CSVRepository("data/lugares_turisticos_argentina.csv")
    return PlaceService(repository=repo)
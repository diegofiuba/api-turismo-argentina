import pandas as pd
import math
from app.repositories.csv_repository import CSVRepository

repo = CSVRepository("data/lugares_turisticos_argentina.csv")

class PlaceService:
   @staticmethod
   def __clean(records):
       clean_records = [] 
       for row in records:
           clean_row = {}
           for k,v in row.items():
               if isinstance(v,float) and math.isnan(v):
                   clean_row[k] = None
               else:
                   clean_row[k] = v
           clean_records.append(clean_row) 
       return clean_records    

   """ Return the places limited by limit """
   @staticmethod
   def get_places(limit: int = 5):
       df = repo.get_places(limit)
       records = df.to_dict(orient="records")
       return PlaceService.__clean(records) 

   """ Return the places associated to the specific province and/or city """
   @staticmethod
   def filter_places(province: str = None, city: str = None):
       df = repo.filter(province = province,city = city)
       records = df.to_dict(orient="records")
       return PlaceService.__clean(records)   
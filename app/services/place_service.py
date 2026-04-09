import pandas as pd
import math
from app.repositories.csv_repository import CSVRepository

repo = CSVRepository("data/lugares_turisticos_argentina.csv")

class PlaceService:
   
   """ Return the places limited by limit """
   @staticmethod
   def get_places(limit: int = 5):
       df = repo.get_places(limit)

       #df = df.where(pd.notnull(df), None)
       records = df.to_dict(orient="records")

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
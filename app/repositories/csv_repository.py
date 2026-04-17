import pandas as pd
from app.repositories.base_repository import BaseRepository

class CSVRepository(BaseRepository):
   def __init__(self,file_path: str):
       self.df = pd.read_csv(file_path)
   
   """ Return places from the repository """
   def get_places(self) -> pd.DataFrame:
       return self.df
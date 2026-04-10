import pandas as pd

class CSVRepository:
   def __init__(self,file_path: str):
       self.df = pd.read_csv(file_path)
   
   """ Return places from the repository """
   def get_places(self):
       return self.df
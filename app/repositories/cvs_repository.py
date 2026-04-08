import pandas as pd

class CSVRepository:
   def __init__(self,file_path: str):
       self.df = pd.read_csv(file_path)

   """ Return the first n places from the repository """
   def get_places(self,n):
       return self.df.head(n)

   """ Return places filter by key and value passed by argument """
   def filter(self, **kwargs):
       df = self.df
       for key, value in kwargs.items():
           if value:
               df = df[df[key].str.lower() == value.lower()]
       return df

   """ Return places that contains the text passed by argument """
   def search(self,query:str):
       return self.df[self.df["name"].str.contains(query,case=False,na=False)] 
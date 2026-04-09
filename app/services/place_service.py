import pandas as pd
import numpy as np
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

	""" Search and returns places that contain the words passed by parameter """
	@staticmethod
	def search_places(query: str):
	   df = repo.search(query)
	   records = df.to_dict(orient="records")
	   return PlaceService.__clean(records)
	   
	""" Returns places close to the given latitude and longitude and within a given radius """   
	@staticmethod
	def get_nearby_places(latitude: float, longitude: float, radius: float = 10):

		# haversine distance formula

		R = 6371  # earth radius in km

		# conversion from degrees to radians
		lat1 = np.radians(latitude)
		lon1 = np.radians(longitude)

		# conversion from degrees to radians
		lat2 = np.radians(repo.df["latitude"])
		lon2 = np.radians(repo.df["longitude"])

		delta_lat = lat2 - lat1
		delta_lon = lon2 - lon1

		a = (
			np.sin(delta_lat  / 2) ** 2
			+ np.cos(lat1) * np.cos(lat2) * np.sin(delta_lon / 2) ** 2
		)

		c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))

		distance = R * c

		# filter by radius
		nearby_places = repo.df[distance <= radius]

		# add column to filtered dataframe 
		nearby_places["distance_km"] = distance[distance <= radius]         

		# sort by proximity
		nearby_places  = nearby_places.sort_values(by="distance_km")

		records = nearby_places.to_dict(orient="records")
		return PlaceService.__clean(records)
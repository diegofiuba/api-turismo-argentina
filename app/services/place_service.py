import pandas as pd
import numpy as np
import math
from app.repositories.base_repository import BaseRepository

class PlaceService:
    def __init__(self,repository: BaseRepository):
        self.repository = repository

    def __clean(self,records):
        clean_records = []
        for row in records:
            clean_row = {}
            for k, v in row.items():
                if isinstance(v, float) and math.isnan(v):
                    clean_row[k] = None
                else:
                    clean_row[k] = v
            clean_records.append(clean_row)
        return clean_records

    """ Return places """
    def get_places(self,
        limit: int = 10,
        offset: int = 0,
        province: str = None,
        city: str = None,
        keywords: str = None,
        latitude: float = None,
        longitude: float = None,
        radius: float = None
    ):
        df = self.repository.get_places()

        # filter places
        if province:
            df = df[df["province"].str.lower() == province.lower()]

        if city:
            df = df[df["city"].str.lower() == city.lower()]

        # search places
        if keywords:
            df = df[df["name"].str.contains(keywords, case=False, na=False)]

        # nearby places
        if latitude is not None and longitude is not None and radius is not None:
            R = 6371  # earth radius in km

            # conversion from degrees to radians
            lat1 = np.radians(latitude)
            lon1 = np.radians(longitude)

            lat2 = np.radians(df["latitude"])
            lon2 = np.radians(df["longitude"])

            delta_lat = lat2 - lat1
            delta_lon = lon2 - lon1

            a = (
                np.sin(delta_lat / 2) ** 2
                + np.cos(lat1) * np.cos(lat2) * np.sin(delta_lon / 2) ** 2
            )

            c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
            distance = R * c

            # filter by radius
            df = df[distance <= radius].copy()

            # add column to filtered dataframe
            df["distance_km"] = distance[distance <= radius]

            # sort by proximity
            df = df.sort_values(by="distance_km")

        total = len(df)			
			
        # pagination			
        df = df.iloc[ offset : offset+limit ]
        		
        records = self.__clean(df.to_dict(orient="records"))
        return {
            "success": True,
            "message": "Places retrieved successfully",
            "data": records,
            "pagination":{
                 "total": total,
                 "limit": limit,
                 "offset": offset,
                 "has_next": offset + limit < total,
                 "has_prev": offset > 0				 
			} 			
		}
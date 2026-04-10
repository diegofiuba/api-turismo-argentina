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
            for k, v in row.items():
                if isinstance(v, float) and math.isnan(v):
                    clean_row[k] = None
                else:
                    clean_row[k] = v
            clean_records.append(clean_row)
        return clean_records

    """ Return places """
    @staticmethod
    def get_places(
        limit: int = 10,
        offset: int = 0,
        province: str = None,
        city: str = None,
        keywords: str = None,
        latitude: float = None,
        longitude: float = None,
        radius: float = None
    ):
        df = repo.df

        # filter places
        if province:
            df = df[df["province"].str.lower() == province.lower()]

        if city:
            df = df[df["city"].str.lower() == city.lower()]

        # search places
        if keywords:
            df = df[df["name"].str.contains(keywords, case=False, na=False)]

        # nearby places
        if latitude and longitude and radius:
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

        # pagination			
        df = df.iloc[ offset : offset+limit ]
        		
        records = df.to_dict(orient="records")
        return PlaceService.__clean(records)
# Argentina Tourist Places API

> API REST to search for tourist sites in Argentina

## Features

- List of tourist attractions
- Search by keywords
- Filters by city and province
- Nearby search using geographic coordinates
- Pagination support (limit & offset)

## Data structure 

The data source is a CSV dataset containing:

- name
- type
- latitude
- longitude
- province
- city

## Endpoints

### GET /places

Return a list of tourist places.

Support query parameters for:

- keywords &rarr; search by name
- city &rarr; filter by city
- province &rarr; filter by province
- latitude &rarr; latitude for nearby search
- longitude &rarr; longitude for nearby search
- radius &rarr; radius in km
- limit &rarr; number of results (default:10)
- offset &rarr; pagination offset

### Example Request

```http
GET /places?keywords=cerro
GET /places?city=salta
GET /places?latitude=-34.6&longitude=-58.38&radius=50
GET /places/?keywords=glaciar%20perito%20moreno&latitude=-50.4690325&longitude=-73.0298567&radius=0
```

### Example Response

```http
{
  "success":true,
  "message":"Places retrieved successfully",
  "data":[
   {
     "name":"Glaciar Perito Moreno",
	 "type":"attraction",
	 "latitude":-50.4690325,
	 "longitude":-73.0298567,
	 "province":null,
	 "city":null,
	 "distance_km":0.0
   }
  ],
  "pagination": {
    "total":1,
	"limit":10,
	"offset":0,
	"has_next":false,
	"has_prev":false
  }
}
```

## How to run

pip install -r requirements.txt<br>
uvicorn main:app --reload

## Example of usage

curl "http://localhost:8000/places?keywords=cerro"

## Architecture

- Router: handles HTTP requests and validation
- Service: contain business logic (filter, search, distance calculation)
- Repository: abstract data access (currently CSV)
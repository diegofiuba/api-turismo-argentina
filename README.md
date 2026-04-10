# Argentina Tourist Places API

> API REST to search for tourist sites in Argentina

## Features

- List of tourist attractions
- Search by name
- Filters by city and province
- Nearby search using geographic coordinates

## Data structure 

The data source is a CSV file containing:

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

- keywords
- city
- province
- latitude
- longitude
- radius
- limit
- offset

### Examples

```http
GET /places?keywords=cerro
GET /places?city=salta
GET /places?latitude=-34.6&longitude=-58.38&radius=50
```

## How to run

pip install -r requirements.txt<br>
uvicorn main:app --reload

## Example of usage

curl "http://localhost:8000/places?keywords=cerro"

## Architecture

- Router: handles HTTP requests
- Service: business logic (filter, search, distance calculation)
- Repository: data access layer (CSV)
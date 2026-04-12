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

- Router: handles HTTP requests and validation
- Service: contain business logic (filter, search, distance calculation)
- Repository: abstract data access (currently CSV)
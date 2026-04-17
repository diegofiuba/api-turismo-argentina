from fastapi import FastAPI, Depends
from app.routes import places

app = FastAPI(title="API de turismo de Argentina")

app.include_router(places.router,prefix="/places",tags=["Places"])

@app.get("/")
def root():
    return {"message": "Bienvenido a la API de turismo de Argenina"}
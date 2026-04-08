from fastapi import FastAPI

app = FastAPI(title="API de turismo de Argentina")

@app.get("/")
def root():
    return {"message": "Bienvenido a la API de turismo de Argenina"}
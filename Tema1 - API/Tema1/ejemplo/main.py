from routers import Empleado, Tienda
from fastapi import FastAPI

app = FastAPI()

# Routers
app.include_router(Empleado.router)
app.include_router(Tienda.router)

@app.get("/")
def root():
    return {"Hello": "World"}
from routers import Alumnos, Colegio
from routers import auth_users, Alumnos_db
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Routers
app.include_router(Colegio.router)
app.include_router(Alumnos.router)
app.include_router(auth_users.router)
app.include_router(Alumnos_db.router)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def root():
    return {"Hello": "World"}
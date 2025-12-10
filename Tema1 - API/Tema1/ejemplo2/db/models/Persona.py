
from typing import Optional
from pydantic import BaseModel

# Entidad persona
class Persona(BaseModel):
    id: str | None = None
    DNI: str
    Nombre: str
    Apellidos: str
    Telefono: str
    Correo: str

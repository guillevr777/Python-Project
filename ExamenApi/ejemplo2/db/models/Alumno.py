
from typing import Optional
from pydantic import BaseModel

# Entidad persona
class Alumno(BaseModel):
    id: str | None = None
    nombre: str
    apellidos: str
    fecha_nacimiento: str
    curso: str
    repetidor: bool
    id_colegio: str

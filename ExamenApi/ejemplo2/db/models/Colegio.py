
from typing import Optional
from pydantic import BaseModel

# Entidad movil
class Colegio(BaseModel):
    id: Optional[str] = None
    nombre: str
    distrito: str
    tipo: str
    direccion: str
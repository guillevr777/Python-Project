
from typing import Optional
from pydantic import BaseModel

# Entidad movil
class Movil(BaseModel):
    id: Optional[str] = None
    PrecioCoste: float
    PrecioVenta: float
    IdPersona: str
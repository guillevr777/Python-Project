from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/moviles", tags=["moviles"])

class Movil(BaseModel):
    Id: int
    PrecioCoste: float
    PrecioVenta: float
    IdPersona: int

moviles_list = [
    Movil(Id=1, PrecioCoste=200.0, PrecioVenta=300.0, IdPersona=1),
    Movil(Id=2, PrecioCoste=250.0, PrecioVenta=350.0, IdPersona=2),
    Movil(Id=3, PrecioCoste=300.0, PrecioVenta=450.0, IdPersona=3),
    Movil(Id=4, PrecioCoste=150.0, PrecioVenta=250.0, IdPersona=4),
    Movil(Id=5, PrecioCoste=400.0, PrecioVenta=550.0, IdPersona=5),
    Movil(Id=6, PrecioCoste=220.0, PrecioVenta=320.0, IdPersona=1),
    Movil(Id=7, PrecioCoste=270.0, PrecioVenta=370.0, IdPersona=2),
    Movil(Id=8, PrecioCoste=320.0, PrecioVenta=470.0, IdPersona=3),
    Movil(Id=9, PrecioCoste=180.0, PrecioVenta=280.0, IdPersona=4),
    Movil(Id=10, PrecioCoste=420.0, PrecioVenta=570.0, IdPersona=5)
]

@router.get("/")
def moviles():
    return moviles_list

@router.get("/{id}")
def movil_id(id: int):
    moviles = [movil for movil in moviles_list if movil.Id == id]

    if len(moviles) != 0:
        return moviles[0]
    else:
        raise HTTPException(status_code=404, detail="Móvil no encontrado")
    
@router.delete("/{id}")
def eliminar_movil(id: int):
    for index, movil in enumerate(moviles_list):
        if movil.Id == id:
            del moviles_list[index]
            return {"message": "Móvil eliminado correctamente"}
    raise HTTPException(status_code=404, detail="Móvil no encontrado")

@router.post("/")
def crear_movil(movil: Movil):
    moviles_list.append(movil)
    return movil

@router.put("/{id}")
def actualizar_movil(id: int, movil_actualizado: Movil):
    for index, movil in enumerate(moviles_list):
        if movil.Id == id:
            moviles_list[index] = movil_actualizado
            return movil_actualizado
    raise HTTPException(status_code=404, detail="Móvil no encontrado")

@router.get("/por-persona/{id_persona}")
def moviles_por_persona(id_persona: int):
    moviles_encontrados = [movil for movil in moviles_list if movil.IdPersona == id_persona]
    return moviles_encontrados

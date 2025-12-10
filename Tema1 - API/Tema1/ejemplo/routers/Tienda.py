#TIENDA (Id, Domicilio, Teléfono, PrecioAlquiler)
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/tienda", tags=["tienda"])

class Tienda(BaseModel):
    id: int
    domicilio: str
    telefono: int
    precio_alquiler: float

tiendas_list = [
    Tienda(id=1, domicilio="Calle Falsa 123", telefono=123456789, precio_alquiler=1500.0),
    Tienda(id=2, domicilio="Avenida Siempre Viva 742", telefono=987654321, precio_alquiler=2000.0),
    Tienda(id=3, domicilio="Plaza Mayor 1", telefono=555666777, precio_alquiler=2500.0),
    Tienda(id=4, domicilio="Calle Luna 45", telefono=444555666, precio_alquiler=1800.0),
    Tienda(id=5, domicilio="Calle Sol 67", telefono=333444555, precio_alquiler=2200.0),
    Tienda(id=6, domicilio="Avenida del Mar 89", telefono=222333444, precio_alquiler=3000.0),
    Tienda(id=7, domicilio="Calle Montaña 10", telefono=111222333, precio_alquiler=1600.0),
    Tienda(id=8, domicilio="Calle Río 11", telefono=999888777, precio_alquiler=2700.0)
]

@router.get("/tiendas")
def tiendas():
    return tiendas_list

@router.get("/tiendas/{id}")
def tienda_id(id: int):
    tiendas = [tienda_id for tienda_id in tiendas_list if tienda_id.id == id]

    if len(tiendas) != 0:
        return tiendas[0]
    else:
        raise HTTPException(status_code=404, detail="Tienda no encontrada")

@router.delete("/tiendas/{id}")
def eliminar_tienda(id: int):
    for index, tienda in enumerate(tiendas_list):
        if tienda.id == id:
            del tiendas_list[index]
            return {"message": "Tienda eliminada correctamente"}
    raise HTTPException(status_code=404, detail="Tienda no encontrada")

@router.post("/tiendas")
def crear_tienda(tienda: Tienda):
    tiendas_list.append(tienda)
    return tienda

@router.put("/tiendas/{id}")
def actualizar_tienda(id: int, tienda_actualizada: Tienda):
    for index, tienda in enumerate(tiendas_list):
        if tienda.id == id:
            tiendas_list[index] = tienda_actualizada
            return tienda_actualizada
    raise HTTPException(status_code=404, detail="Tienda no encontrada")

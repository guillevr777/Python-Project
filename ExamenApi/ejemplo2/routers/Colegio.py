from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/Colegios", tags=["Colegios"])

class Colegio(BaseModel):
    id: str
    nombre: str
    distrito: str
    tipo: str
    direccion: str
    
colegios_list = [
    Colegio(id="1", nombre="Nervion", distrito="Nervion", tipo="publico", direccion= "calle Pirineos")
]

@router.get("/")
def colegios():
    return colegios_list

@router.get("/{id}")
def colegio_id(id: str):
    colegios = [colegio for colegio in colegios_list if colegio.Id == id]

    if len(colegios) != 0:
        return colegios[0]
    else:
        raise HTTPException(status_code=404, detail="Móvil no encontrado")
    
@router.delete("/{id}")
def eliminar_movil(id: str):
    for index, colegio in enumerate(colegios_list):
        if colegio.Id == id:
            del colegios_list[index]
            return {"message": "Móvil eliminado correctamente"}
    raise HTTPException(status_code=404, detail="Móvil no encontrado")

@router.post("/")
def crear_colegio(colegio: Colegio):
    colegios_list.append(colegio)
    return colegio

@router.put("/{id}")
def actualizar_movil(id: str, colegio_actualizado: Colegio):
    for index, colegio in enumerate(colegios_list):
        if colegio.Id == id:
            colegios_list[index] = colegios_list
            return colegios_list
    raise HTTPException(status_code=404, detail="colegio no encontrado")


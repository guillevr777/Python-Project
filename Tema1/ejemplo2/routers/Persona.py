from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from routers.Movil import moviles_list
from .auth_users import authentication

router = APIRouter(prefix="/personas", tags=["personas"])

class Persona(BaseModel):
    Id: int 
    DNI: str
    Nombre: str
    Apellidos: str
    Teléfono : int 
    Correo : str

personas_list = [
    Persona(Id=1, DNI="12345678A", Nombre="Ana", Apellidos="López", Teléfono=612345678, Correo="guillevr7@gmail.com"),
    Persona(Id=2, DNI="87654321B", Nombre="Carlos", Apellidos="Sánchez", Teléfono=698765432, Correo="guillevr7@gmail.com"),
    Persona(Id=3, DNI="11223344C", Nombre="Elena", Apellidos="Gómez", Teléfono=634567890, Correo="guillevr7@gmail.com"),
    Persona(Id=4, DNI="44332211D", Nombre="Miguel", Apellidos="Fernández", Teléfono=677889900, Correo="guillevr7@gmail.com"),
    Persona(Id=5, DNI="55667788E", Nombre="Sofía", Apellidos="Martínez", Teléfono=612398765, Correo="guillevr7@gmail.com")
]

@router.get("/")
def personas():
    return personas_list

@router.get("/{id}")
def persona_id(id: int):
    personas = [persona for persona in personas_list if persona.Id == id]

    if len(personas) != 0:
        return personas[0]
    else:
        raise HTTPException(status_code=404, detail="Persona no encontrada")
    
@router.delete("/{id}")
def eliminar_persona(id: int):
    for index, persona in enumerate(personas_list):
        if persona.Id == id:
            del personas_list[index]
            return {"message": "Persona eliminada correctamente"}
    raise HTTPException(status_code=404, detail="Persona no encontrada")

@router.post("/")
def crear_persona(persona: Persona, authorized = Depends(authentication)):
    personas_list.append(persona)
    return persona

@router.put("/{id}")
def actualizar_persona(id: int, persona_actualizada: Persona):
    for index, persona in enumerate(personas_list):
        if persona.Id == id:
            personas_list[index] = persona_actualizada
            return persona_actualizada
    raise HTTPException(status_code=404, detail="Persona no encontrada")

@router.get("/por-movil/{id_movil}")
def personas_por_movil(id_movil: int):
    personas_encontradas = [persona for persona in personas_list if persona.Id == id_movil]
    return personas_encontradas
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from routers.Colegio import colegios_list
from .auth_users import authentication

router = APIRouter(prefix="/Alumnos", tags=["Alumnos"])

class Alumno(BaseModel):
    id: str 
    nombre: str
    apellidos: str
    fecha_nacimiento : str 
    curso : str
    repetidor: bool
    id_colegio: str
    
alumnos_list = [
    Alumno(id="1", nombre="Ana", apellidos="López", fecha_nacimiento="2004/03/07", curso="primero", repetidor=True, id_colegio= "1")
]

@router.get("/")
def alumnos():
    return alumnos_list

@router.get("/{curso}")
def curso_alumnos(curso: str):
    alumnos = [alumno for alumno in curso_alumnos if alumno.curso == curso]

    if len(alumnos) != 0:
        return alumnos[0]
    else:
        raise HTTPException(status_code=404, detail="Alumnos no encontrados")
    
    
@router.delete("/{id}")
def eliminar_alumno(id: str):
    for index, alumno in enumerate(alumnos_list):
        if alumno.Id == id:
            del alumnos_list[index]
            return {"message": "Alumno eliminado correctamente"}
    raise HTTPException(status_code=404, detail="Alumno no encontrado")

@router.post("/")
def crear_alumno(alumno: Alumno, authorized = Depends(authentication)):
    alumnos_list.append(alumno)
    return alumno

@router.put("/{id}")
def actualizar_alumno(id: str, alumno_actualizada: Alumno):
    for index, alumno in enumerate(alumnos_list):
        if alumno.Id == id:
            alumnos_list[index] = alumno_actualizada
            return alumno_actualizada
    raise HTTPException(status_code=404, detail="Alumno no encontrada")

@router.get("/por-colegio/{id_colegio}")
def personas_por_colegio(id_colegio: str):
    alumnos_encontrados = [alumno for alumno in alumnos_list if alumno.id_colegio == id_colegio]
    return alumnos_encontrados
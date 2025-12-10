from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from routers.Tienda import tiendas_list

router = APIRouter(prefix="/empleado", tags=["empleado"])

class Empleado(BaseModel):
    Id: int
    Nombre: str
    Apellidos: str
    Teléfono: int
    Correo: str
    NumCuenta: str
    IdTienda: int

empleados_list = [
    Empleado(Id=1, Nombre="Juan", Apellidos="Pérez", Teléfono=123456789, Correo="guillevr7@gmail.com", NumCuenta="ES12345678901234567890", IdTienda =5),
    Empleado(Id=2, Nombre="María", Apellidos="García", Teléfono=987654321, Correo="pepe@gmail.com", NumCuenta="ES09876543210987654321", IdTienda=2),
    Empleado(Id=3, Nombre="Luis", Apellidos="Martínez", Teléfono=555666777, Correo="yamy@gmail.com", NumCuenta="ES11223344556677889900", IdTienda=3)
]

@router.get("/empleados")
def empleados():
    return empleados_list

@router.get("/empleados/{id}")
def empleado_id(id: int):
    empleados = [empleado for empleado in empleados_list if empleado.Id == id]

    if len(empleados) != 0:
        return empleados[0]
    else:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")
    
@router.delete("/empleados/{id}")
def eliminar_empleado(id: int):
    for index, empleado in enumerate(empleados_list):
        if empleado.Id == id:
            del empleados_list[index]
            return {"message": "Empleado eliminado correctamente"}
    raise HTTPException(status_code=404, detail="Empleado no encontrado")

@router.post("/empleados")
def crear_empleado(empleado: Empleado):
    tienda_ids = [tienda.id for tienda in tiendas_list]
    if empleado.IdTienda not in tienda_ids:
        raise HTTPException(status_code=400, detail="La tienda asociada no existe")
    
    empleados_list.append(empleado)
    return empleado

@router.put("/empleados/{id}")
def actualizar_empleado(id: int, empleado_actualizado: Empleado):
    for index, empleado in enumerate(empleados_list):
        if empleado.Id == id:
            empleados_list[index] = empleado_actualizado
            return empleado_actualizado
    raise HTTPException(status_code=404, detail="Empleado no encontrado")

@router.get("/por-tienda/{id_tienda}")
def empleados_por_tienda(id_tienda: int):
    empleados = [e for e in empleados_list if e.IdTienda == id_tienda]
    if not empleados:
        raise HTTPException(status_code=404, detail="No hay empleados en esta tienda")
    return empleados

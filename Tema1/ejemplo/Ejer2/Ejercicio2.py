#TIENDA (Id, Domicilio, Teléfono, PrecioAlquiler)
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Empleado(BaseModel):
    id: int
    nombre: str
    apellido: str
    telefono: int
    correo: str
    numCuenta: int
    id_empleado: int

empleados_list = [
    Empleado(id = 1, nombre = "pablo", apellido = "Lopez", telefono = 678987656, correo = "Lopez@gmail.com", numCuenta = 12345678, id_tienda = 1)
]

@app.get("/empleados")
def empleados():
    return empleados_list

@app.get("/empleados/{id}")
def empleado_id(id: int):
    empleados = search_empleado(id)

    if len(empleados) != 0:
        return empleados[0]
    raise HTTPException(status_code=404, detail="Empleado no encontrada")

@app.post("/empleados", status_code=201, response_model=Empleado)
def add_empleado(empleado: Empleado):
    empleado.id = next_id()
    empleados_list.append(empleado)
    return empleado

@app.put("/empleados/{id}", response_model=Empleado)
def modify_empleado(id: int, empleado: Empleado):
    for index, saved_empleado in enumerate(empleados_list):
        if saved_empleado == id:
            empleado.id = id
            empleados_list[index] = empleado
            return empleado

@app.delete("/empleados/{id}", status_code=204)
def delete_empleado(id: int):
    for saved_empleado in empleados_list:
        if saved_empleado.id == id:
            empleados_list.remove(saved_empleado)
            return {}
    raise HTTPException(status_code=404, detail="Empleado no encontrada")

def search_empleado(id: int):
    empleados = [empleado for empleado in empleados_list if empleado.id == id]
   
    if len(empleados) != 0:
        return empleados[0]
    else:
        return "Error: No se ha encontrado la empleado"
    
def next_id():
    return max(empleados, key=id).id+1
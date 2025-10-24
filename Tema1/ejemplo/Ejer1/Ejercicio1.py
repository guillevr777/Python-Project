#TIENDA (Id, Domicilio, Teléfono, PrecioAlquiler)
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

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

@app.get("/tiendas")
def tiendas():
    return tiendas_list

@app.get("/tiendas/{id}")
def tienda_id(id: int):
    tiendas = search_tienda(id)

    if len(tiendas) != 0:
        return tiendas[0]
    raise HTTPException(status_code=404, detail="Tienda no encontrada")

@app.post("/tiendas", status_code=201, response_model=Tienda)
def add_tienda(tienda: Tienda):
    tienda.id = next_id()
    tiendas_list.append(tienda)
    return tienda

@app.put("/tiendas/{id}", response_model=Tienda)
def modify_tienda(id: int, tienda: Tienda):
    for index, saved_tienda in enumerate(tiendas_list):
        if saved_tienda == id:
            tienda.id = id
            tiendas_list[index] = tienda
            return tienda

@app.delete("/tiendas/{id}", status_code=204)
def delete_tienda(id: int):
    for saved_tienda in tiendas_list:
        if saved_tienda.id == id:
            tiendas_list.remove(saved_tienda)
            return {}
    raise HTTPException(status_code=404, detail="Tienda no encontrada")

def search_tienda(id: int):
    tiendas = [tienda for tienda in tiendas_list if tienda.id == id]

    if len(tiendas) != 0:
        return tiendas[0]
    else:
        return "Error: No se ha encontrado la tienda"
    
def next_id():
    if tiendas_list:  # verifica que la lista no esté vacía
        return max(tienda.id for tienda in tiendas_list) + 1
    return 1    
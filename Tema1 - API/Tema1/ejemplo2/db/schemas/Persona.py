def user_schema(Persona) -> dict:
    # El id en base de datos es _id
    return {"id": str(Persona["_id"]),
            "DNI": Persona["DNI"],
            "Nombre": Persona["Nombre"],
            "Apellidos": Persona["Apellidos"],
            "Telefono": Persona["Telefono"],
            "Correo": Persona["Correo"]}

def users_schema(Personas) -> list:
    return [user_schema(Persona) for  Persona in Personas]
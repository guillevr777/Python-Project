def user_schema(Colegio) -> dict:

    return {"nombre": str(Colegio["nombre"]),
            "distrito": Colegio["distrito"],
            "tipo": Colegio["tipo"],
            "direccion": Colegio["direccion"]}


def users_schema(Colegios) -> list:
    return [user_schema(Colegio) for  Colegio in Colegios]
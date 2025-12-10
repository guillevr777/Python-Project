def user_schema(Movil) -> dict:
    # El id en base de datos es _id
    return {"id": str(Movil["_id"]),
            "PrecioCoste": Movil["PrecioCoste"],
            "PrecioVenta": Movil["PrecioVenta"],
            "IdPersona": Movil["IdPersona"]}


def users_schema(Moviles) -> list:
    return [user_schema(Movil) for  Movil in Moviles]
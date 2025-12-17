def user_schema(Alumno) -> dict:

    return {"id": str(Alumno["_id"]),
            "nombre": Alumno["nombre"],
            "apellidos": Alumno["apellidos"],
            "fecha_nacimiento": Alumno["fecha_nacimiento"],
            "curso": Alumno["curso"],
            "repetidor": Alumno["repetidor"],
            "id_colegio": Alumno["id_colegio"]}


def users_schema(Alumnos) -> list:
    return [user_schema(Alumno) for  Alumno in Alumnos]
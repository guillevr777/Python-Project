import sys

# Proceso 1: Filtra las líneas de salarios.txt por departamento y envía al
# Proceso 2 (a través de stdout/pipe) las líneas que pertenecen a ese
# departamento, SIN incluir el campo de departamento.
#
# Parámetro de entrada: nombre del departamento (sys.argv[1]).
# Solo necesitamos el departamento para filtrar; el fichero siempre es
# salarios.txt (ubicado en el mismo directorio), por lo que no hace falta
# pasarlo como parámetro.
#
# Formato del fichero real: Nombre;Apellido;Salario;Departamento  (sep = ";")
# Formato de salida por stdout: "Apellido Nombre;Salario"
# (se elimina el campo departamento y se reordena a Apellido Nombre)
#
# Comunicación hacia Proceso2: stdout → stdin (pipe gestionado por Main).

departamento = sys.argv[1]

# newline="" + strip() elimina tanto "\n" (Unix) como "\r\n" (Windows)
with open("salarios.txt", "r", encoding="utf-8", newline="") as f:
    for linea in f:
        linea = linea.strip()   # elimina \r\n o \n indistintamente
        if not linea:
            continue

        # Formato del fichero: Nombre;Apellido;Salario;Departamento
        partes = linea.split(";")
        nombre   = partes[0].strip()
        apellido = partes[1].strip()
        salario  = partes[2].strip()
        depto    = partes[3].strip()

        # Filtramos por departamento (comparación insensible a mayúsculas)
        if depto.lower() == departamento.lower():
            # Enviamos al siguiente proceso: "Apellido Nombre;Salario"
            print(f"{apellido} {nombre};{salario}", flush=True)
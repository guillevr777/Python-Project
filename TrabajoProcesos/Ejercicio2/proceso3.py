import sys

# Proceso 3: Lee líneas de stdin (pipe desde Proceso2) con formato
# "Apellido Nombre;Salario" y las escribe en empleados.txt con el formato
# solicitado: "Apellido Nombre, Salario"
#
# No recibe ningún parámetro de línea de comandos:
# - Los datos llegan por stdin (pipe de Proceso2).
# - El fichero de salida siempre se llama empleados.txt (fijo por enunciado).
# Cero argumentos es la mínima cantidad posible, cumpliendo el requisito.
#
# Comunicación: stdin ← pipe de Proceso2.

with open("empleados.txt", "w", encoding="utf-8") as salida:
    for linea in sys.stdin:
        linea = linea.strip()
        if not linea:
            continue

        # Formato recibido: "Apellido Nombre;Salario"  (sep = ";")
        # Formato de salida: "Apellido Nombre, Salario"
        partes = linea.split(";")
        nombre  = partes[0].strip()
        salario = partes[1].strip()

        salida.write(f"{nombre}, {salario}\n")
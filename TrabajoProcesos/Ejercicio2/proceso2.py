import sys

# Proceso 2: Lee líneas de stdin (pipe desde Proceso1) con formato
# "Apellido Nombre;Salario" y reenvía por stdout aquellas cuyo salario
# sea mayor o igual al salario mínimo recibido.
#
# Parámetro de entrada: salario mínimo (float, sys.argv[1]).
# Solo necesitamos el umbral; los datos llegan por stdin, por lo que no hay
# más información que deba pasarse como argumento.
#
# Comunicación: stdin ← pipe de Proceso1 | stdout → pipe hacia Proceso3.
# Las líneas se reenvían TAL COMO llegan (sin modificar), según el enunciado.

salario_minimo = float(sys.argv[1])

for linea in sys.stdin:
    linea = linea.strip()
    if not linea:
        continue

    # Formato recibido: "Apellido Nombre;Salario"  (sep = ";")
    partes = linea.split(";")
    salario = float(partes[-1])  # El salario es siempre el último campo

    # Solo reenviamos si supera o iguala el mínimo
    if salario >= salario_minimo:
        print(linea, flush=True)
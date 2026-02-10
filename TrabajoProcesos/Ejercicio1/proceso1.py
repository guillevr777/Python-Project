import random
import sys
import os

# Proceso 1: Genera 24 temperaturas aleatorias (0.00–20.00) para un día dado
# y las escribe en un fichero cuyo nombre es la fecha (ej: 01-12.txt).
#
# Parámetros de entrada: día (int) y mes (int).
# Se elige pasar solo día y mes porque el proceso únicamente necesita saber
# qué fecha tiene que generar y cómo nombrar el fichero.
# No se pasa el directorio: el fichero se crea en el mismo directorio de trabajo
# del proceso (la carpeta del ejercicio), que es siempre ejercicio1/.

def generar_temperaturas(dia: int, mes: int):
    # Construimos el nombre del fichero con formato DD-MM.txt
    nombre_fichero = f"{dia:02d}-{mes:02d}.txt"

    # Generamos 24 temperaturas con dos decimales en el rango [0.00, 20.00]
    temperaturas = [round(random.uniform(0, 20), 2) for _ in range(24)]

    # Escribimos cada temperatura en una línea del fichero
    with open(nombre_fichero, "w") as f:
        for temp in temperaturas:
            f.write(f"{temp:.2f}\n")


if __name__ == "__main__":
    # Recibimos día y mes como argumentos de línea de comandos
    dia = int(sys.argv[1])
    mes = int(sys.argv[2])
    generar_temperaturas(dia, mes)
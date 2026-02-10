import sys

# Proceso 3: Lee las temperaturas de un fichero (DD-MM.txt) y añade al fichero
# minimas.txt la fecha y la temperatura mínima separadas por dos puntos.
#
# Parámetros de entrada: día (int) y mes (int).
# Misma decisión que en Proceso2: día y mes son suficientes para localizar
# el fichero fuente y construir la etiqueta de fecha.
# Se usa modo append ("a") por la misma razón que en Proceso2.

def calcular_minima(dia: int, mes: int):
    nombre_fichero = f"{dia:02d}-{mes:02d}.txt"
    fecha = f"{dia:02d}-{mes:02d}"

    # Leemos todas las temperaturas del fichero
    with open(nombre_fichero, "r") as f:
        temperaturas = [float(linea.strip()) for linea in f if linea.strip()]

    temperatura_minima = min(temperaturas)

    # Abrimos minimas.txt en modo append para no perder datos de otros procesos
    with open("minimas.txt", "a") as f:
        f.write(f"{fecha}:{temperatura_minima:.2f}\n")


if __name__ == "__main__":
    dia = int(sys.argv[1])
    mes = int(sys.argv[2])
    calcular_minima(dia, mes)
import sys

# Proceso 2: Lee las temperaturas de un fichero (DD-MM.txt) y añade al fichero
# maximas.txt la fecha y la temperatura máxima separadas por dos puntos.
#
# Parámetros de entrada: día (int) y mes (int).
# Igual que en Proceso1, con día y mes construimos el nombre del fichero fuente
# y la etiqueta de fecha para maximas.txt, sin necesitar más información.
# El acceso a maximas.txt se hace en modo append ("a") para que las 31
# ejecuciones simultáneas vayan acumulando resultados sin sobreescribirse.
# NOTA: En un escenario de alta concurrencia se usaría un lock; aquí las
# escrituras son tan breves que la colisión es improbable y el enunciado
# no exige garantía de orden.

def calcular_maxima(dia: int, mes: int):
    nombre_fichero = f"{dia:02d}-{mes:02d}.txt"
    fecha = f"{dia:02d}-{mes:02d}"

    # Leemos todas las temperaturas del fichero
    with open(nombre_fichero, "r") as f:
        temperaturas = [float(linea.strip()) for linea in f if linea.strip()]

    temperatura_maxima = max(temperaturas)

    # Abrimos maximas.txt en modo append para no perder datos de otros procesos
    with open("maximas.txt", "a") as f:
        f.write(f"{fecha}:{temperatura_maxima:.2f}\n")


if __name__ == "__main__":
    dia = int(sys.argv[1])
    mes = int(sys.argv[2])
    calcular_maxima(dia, mes)
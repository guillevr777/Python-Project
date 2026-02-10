import subprocess
import os
import sys

# Main del Ejercicio 1.
#
# Estrategia de lanzamiento:
# 1) Se lanzan 31 procesos Proceso1 de forma SIMULTÁNEA (uno por cada día de
#    diciembre) usando subprocess.Popen y guardando las referencias.
#    Se espera a que todos terminen (wait) antes de pasar al paso 2,
#    garantizando que los 31 ficheros DD-12.txt existen antes de leerlos.
#
# 2) Se lanzan 31 procesos Proceso2 y 31 procesos Proceso3 SIMULTÁNEAMENTE
#    (62 en total) del mismo modo. Proceso2 y Proceso3 leen el mismo fichero
#    pero escriben en ficheros distintos, por lo que no hay conflicto de
#    lectura. La escritura en maximas.txt y minimas.txt se hace en append,
#    lo que permite la concurrencia sin pérdida de datos.
#
# Comunicación: los procesos reciben día y mes por argumentos de línea de
# comandos (sys.argv). Es el mecanismo más sencillo para parámetros simples
# y de solo lectura.
#
# cwd=directorio_ejercicio: asegura que todos los ficheros generados queden
# en la carpeta ejercicio1/, tal como exige el enunciado.

# Directorio donde viven los scripts y donde se crearán los ficheros
DIRECTORIO = os.path.dirname(os.path.abspath(__file__))
MES = 12  # Diciembre


def lanzar_proceso(script: str, dia: int, mes: int) -> subprocess.Popen:
    """Lanza un subproceso Python con el script dado y devuelve el objeto Popen."""
    return subprocess.Popen(
        [sys.executable, script, str(dia), str(mes)],
        cwd=DIRECTORIO  # Los ficheros se crean en la carpeta del ejercicio
    )


def esperar_procesos(procesos: list):
    """Espera a que todos los procesos de la lista terminen."""
    for p in procesos:
        p.wait()


# ─── PASO 1: Generar temperaturas para los 31 días de diciembre ──────────────
print("Lanzando Proceso1 para los 31 días de diciembre...")
procesos_p1 = [lanzar_proceso("Proceso1.py", dia, MES) for dia in range(1, 32)]
esperar_procesos(procesos_p1)
print("Proceso1 finalizado. 31 ficheros de temperaturas creados.")

# ─── PASO 2: Calcular máximas y mínimas de forma simultánea ──────────────────
print("Lanzando Proceso2 y Proceso3 simultáneamente para los 31 días...")

procesos_p2 = [lanzar_proceso("Proceso2.py", dia, MES) for dia in range(1, 32)]
procesos_p3 = [lanzar_proceso("Proceso3.py", dia, MES) for dia in range(1, 32)]

# Esperamos a que TODOS los procesos de ambos grupos terminen
esperar_procesos(procesos_p2)
esperar_procesos(procesos_p3)

print("Proceso2 y Proceso3 finalizados.")
print(f"Resultados en: {os.path.join(DIRECTORIO, 'maximas.txt')}")
print(f"Resultados en: {os.path.join(DIRECTORIO, 'minimas.txt')}")
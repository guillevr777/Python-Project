import subprocess
import sys
import os

# Main del Ejercicio 2.
#
# Arquitectura de comunicación: PIPELINE DE TUBERÍAS (pipes)
# Proceso1 → (stdout|stdin) → Proceso2 → (stdout|stdin) → Proceso3
#
# Se elige pipe porque:
# - Los datos fluyen en una sola dirección y de forma continua.
# - No necesitamos ficheros intermedios (más eficiente y limpio).
# - subprocess.PIPE permite encadenar stdout de un proceso con stdin del
#   siguiente, que es exactamente el patrón productor-filtro-consumidor.
#
# Orden de lanzamiento: Proceso1 → Proceso2 → Proceso3.
# Proceso2 depende de la salida de Proceso1, y Proceso3 de la de Proceso2,
# por lo que el orden es estrictamente secuencial en la CONEXIÓN, aunque
# los tres procesos corren en paralelo una vez arrancados (el pipe gestiona
# la sincronización automáticamente).
#
# El Main espera a que los tres procesos terminen (wait) antes de finalizar.

# Directorio donde viven los scripts y el fichero salarios.txt
DIRECTORIO = os.path.dirname(os.path.abspath(__file__))

# ─── Entrada del usuario ──────────────────────────────────────────────────────
departamento   = input("Introduce el nombre del departamento: ").strip()
salario_minimo = input("Introduce el salario mínimo: ").strip()

# ─── Lanzamiento de la cadena de procesos ────────────────────────────────────

# Proceso 1: filtra por departamento → su stdout se conecta al stdin de P2
p1 = subprocess.Popen(
    [sys.executable, "Proceso1.py", departamento],
    stdout=subprocess.PIPE,
    cwd=DIRECTORIO
)

# Proceso 2: filtra por salario mínimo → su stdin es el stdout de P1
#            su stdout se conecta al stdin de P3
p2 = subprocess.Popen(
    [sys.executable, "Proceso2.py", salario_minimo],
    stdin=p1.stdout,   # Recibe la salida de Proceso1
    stdout=subprocess.PIPE,
    cwd=DIRECTORIO
)

# Una vez conectado p1.stdout a p2.stdin, cerramos la referencia en el padre
# para que p2 reciba EOF cuando p1 termine (buena práctica con pipes).
p1.stdout.close()

# Proceso 3: escribe en empleados.txt → su stdin es el stdout de P2
p3 = subprocess.Popen(
    [sys.executable, "Proceso3.py"],
    stdin=p2.stdout,   # Recibe la salida de Proceso2
    cwd=DIRECTORIO
)

# Igual que antes: cerramos la referencia del padre al stdout de p2
p2.stdout.close()

# ─── Esperar a que todos los procesos terminen ────────────────────────────────
p1.wait()
p2.wait()
p3.wait()

print(f"\nProceso completado.")
print(f"Resultados guardados en: {os.path.join(DIRECTORIO, 'empleados.txt')}")
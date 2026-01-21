import multiprocessing
import time

def contar_vocal(vocal, ruta_fichero):
    """
    Cuenta cuántas veces aparece una vocal en un fichero de texto.
    """
    contador = 0
    with open(ruta_fichero, "r", encoding="utf-8") as fichero:
        for linea in fichero:
            contador += linea.lower().count(vocal)
    print(f"La vocal '{vocal}' aparece {contador} veces")

if __name__ == "__main__":
    ruta_fichero = "fichero1.txt"  # Fichero de texto a analizar
    vocales = ["a", "e", "i", "o", "u"]

    procesos = []

    inicio = time.time()

    for vocal in vocales:
        proceso = multiprocessing.Process(
            target=contar_vocal,
            args=(vocal, ruta_fichero)
        )
        procesos.append(proceso)
        proceso.start()

    for proceso in procesos:
        proceso.join()

    fin = time.time()

    print(f"\nTiempo total de ejecución: {fin - inicio:.4f} segundos")
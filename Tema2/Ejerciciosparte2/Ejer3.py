import multiprocessing
import random
import time
import os


def proceso_1(ruta_fichero):
    """
    Genera 6 notas decimales entre 1 y 10 y las guarda en un fichero.
    """
    with open(ruta_fichero, "w", encoding="utf-8") as f:
        for _ in range(6):
            nota = round(random.uniform(1, 10), 2)
            f.write(f"{nota}\n")


def proceso_2(args):
    """
    Calcula la media de las notas de un alumno y la guarda en medias.txt
    """
    ruta_fichero, nombre_alumno = args

    with open(ruta_fichero, "r", encoding="utf-8") as f:
        notas = [float(linea.strip()) for linea in f]

    media = sum(notas) / len(notas)

    with open("medias.txt", "a", encoding="utf-8") as f:
        f.write(f"{media:.2f} {nombre_alumno}\n")


def proceso_3():
    """
    Lee medias.txt y muestra la nota máxima y el alumno correspondiente.
    """
    nota_maxima = -1
    alumno_max = ""

    with open("medias.txt", "r", encoding="utf-8") as f:
        for linea in f:
            nota, alumno = linea.strip().split()
            nota = float(nota)

            if nota > nota_maxima:
                nota_maxima = nota
                alumno_max = alumno

    print(f"Nota máxima: {nota_maxima:.2f} - Alumno: {alumno_max}")


if __name__ == "__main__":
    inicio = time.time()

    if os.path.exists("medias.txt"):
        os.remove("medias.txt")

    ficheros = [f"Alumno{i}.txt" for i in range(1, 11)]

    with multiprocessing.Pool() as pool:
        pool.map(proceso_1, ficheros)

    tareas = [(f"Alumno{i}.txt", f"Alumno{i}") for i in range(1, 11)]

    with multiprocessing.Pool() as pool:
        pool.map(proceso_2, tareas)

    proceso_3()

    fin = time.time()
    print(f"\nTiempo total de ejecución: {fin - inicio:.4f} segundos")

import multiprocessing
import datetime
import os


def proceso_1(ruta_fichero, año, cola_salida):
    """
    Lee el fichero de películas y envía por la cola
    aquellas estrenadas en el año indicado.
    """
    with open(ruta_fichero, "r", encoding="utf-8") as f:
        for linea in f:
            nombre, año_pelicula = linea.strip().split(";")
            if int(año_pelicula.strip()) == año:   # ← pequeño extra de seguridad
                cola_salida.put(f"{nombre};{año_pelicula.strip()}")

    # Señal de fin
    cola_salida.put(None)


def proceso_2(año, cola_entrada):
    """
    Recibe películas y las guarda en el fichero peliculasXXXX.txt
    en la MISMA carpeta donde está el script.
    """
    # 📌 Ruta absoluta de la carpeta del proyecto (donde está este .py)
    carpeta_proyecto = os.path.dirname(os.path.abspath(__file__))

    nombre_fichero = os.path.join(carpeta_proyecto, f"peliculas{año}.txt")

    with open(nombre_fichero, "w", encoding="utf-8") as f:
        while True:
            pelicula = cola_entrada.get()
            if pelicula is None:
                break
            f.write(pelicula + "\n")


if __name__ == "__main__":
    # -------- MAIN --------
    año_actual = datetime.datetime.now().year

    año = int(input("Introduce un año (menor que el actual): "))
    while año >= año_actual:
        año = int(input("Año no válido. Introduce un año menor que el actual: "))

    ruta_fichero = input("Introduce la ruta del fichero de películas: ")

    cola = multiprocessing.Queue()

    p1 = multiprocessing.Process(
        target=proceso_1,
        args=(ruta_fichero, año, cola)
    )

    p2 = multiprocessing.Process(
        target=proceso_2,
        args=(año, cola)
    )

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(f"\nProceso finalizado. Películas guardadas en peliculas{año}.txt")

from multiprocessing import Process, Queue
import time

def leer_fichero(ruta_fichero, cola):
    """
    Lee números de un fichero (uno por línea)
    y los introduce en la cola.
    """
    with open(ruta_fichero, "r") as fichero:
        for linea in fichero:
            numero = int(linea.strip())
            cola.put(numero)

    # Señal de fin
    cola.put(None)


def sumar_desde_cola(cola):
    """
    Lee números de la cola y calcula la suma
    desde 1 hasta cada número recibido.
    """
    while True:
        numero = cola.get()
        if numero is None:
            break

        resultado = sum(range(1, numero + 1))
        print(f"Suma de 1 a {numero}: {resultado}")


if __name__ == "__main__":

    cola = Queue()

    # ⏱ Inicio del tiempo
    inicio = time.perf_counter()

    # Crear procesos
    p_lector = Process(target=leer_fichero, args=("numeros.txt", cola))
    p_sumador = Process(target=sumar_desde_cola, args=(cola,))

    p_lector.start()
    p_sumador.start()

    p_lector.join()
    p_sumador.join()

    # ⏱ Fin del tiempo
    fin = time.perf_counter()

    print(f"\nTiempo total de ejecución: {fin - inicio:.4f} segundos")
    print("Todos los procesos han terminado")

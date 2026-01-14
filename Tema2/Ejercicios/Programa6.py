import multiprocessing
import time

# Función que lee números de un archivo y los pone en la cola
def leer_numeros(fichero, cola):
    with open(fichero, "r") as f:
        for linea in f:
            numeros = linea.strip().split()
            if len(numeros) == 2:
                a, b = map(int, numeros)
                cola.put((a, b))  # Se envía la tupla a la cola
    # Señal de fin
    cola.put(None)  # Indicamos que no hay más datos

# Función que toma números de la cola y realiza la suma
def sumar_desde_cola(cola):
    while True:
        item = cola.get()  # Espera hasta que haya un elemento
        if item is None:  # Señal de fin
            break
        a, b = item
        inicio = min(a, b)
        fin = max(a, b)
        resultado = sum(range(inicio, fin + 1))
        print(f"Suma de {a} a {b}: {resultado}")

if __name__ == "__main__":
    fichero = "numeros.txt"  # Archivo de ejemplo con dos números por línea

    # Crear la cola
    cola = multiprocessing.Queue()

    # Guardamos el tiempo de inicio
    tiempo_inicio = time.time()

    # Crear procesos
    proceso_lector = multiprocessing.Process(target=leer_numeros, args=(fichero, cola))
    proceso_sumador = multiprocessing.Process(target=sumar_desde_cola, args=(cola,))

    # Iniciar procesos
    proceso_lector.start()
    proceso_sumador.start()

    # Esperar a que terminen
    proceso_lector.join()
    proceso_sumador.join()

    # Tiempo de fin
    tiempo_fin = time.time()
    print("Todos los procesos han terminado.")
    print(f"Tiempo total de ejecución: {tiempo_fin - tiempo_inicio:.4f} segundos")

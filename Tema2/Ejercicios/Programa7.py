import multiprocessing
import time

# Función que lee números de un archivo y los envía por la pipe
def leer_numeros_pipe(fichero, conn):
    with open(fichero, "r") as f:
        for linea in f:
            numeros = linea.strip().split()
            if len(numeros) == 2:
                a, b = map(int, numeros)
                conn.send((a, b))  # Enviar la tupla por la pipe
    # Señal de fin
    conn.send(None)  # Indicamos que no hay más datos
    conn.close()  # Cerramos la conexión

# Función que recibe números de la pipe y realiza la suma
def sumar_desde_pipe(conn):
    while True:
        item = conn.recv()  # Recibir datos de la pipe
        if item is None:  # Señal de fin
            break
        a, b = item
        inicio = min(a, b)
        fin = max(a, b)
        resultado = sum(range(inicio, fin + 1))
        print(f"Suma de {a} a {b}: {resultado}")
    conn.close()

if __name__ == "__main__":
    fichero = "numeros.txt"  # Archivo de ejemplo con dos números por línea

    # Crear la pipe
    parent_conn, child_conn = multiprocessing.Pipe()

    # Guardamos el tiempo de inicio
    tiempo_inicio = time.time()

    # Crear procesos
    proceso_lector = multiprocessing.Process(target=leer_numeros_pipe, args=(fichero, child_conn))
    proceso_sumador = multiprocessing.Process(target=sumar_desde_pipe, args=(parent_conn,))

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

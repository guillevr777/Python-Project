from multiprocessing import Process, Pipe
import time

def leer_fichero(ruta_fichero, conn):
    """
    Lee números de un fichero y los envía al proceso sumador
    usando una tubería (Pipe).
    """
    with open(ruta_fichero, "r") as fichero:
        for linea in fichero:
            numero = int(linea.strip())
            conn.send(numero)

    # Señal de fin
    conn.send(None)
    conn.close()


def sumar_desde_pipe(conn):
    """
    Recibe números desde la tubería y realiza la suma
    desde 1 hasta cada número recibido.
    """
    while True:
        numero = conn.recv()
        if numero is None:
            break

        resultado = sum(range(1, numero + 1))
        print(f"Suma de 1 a {numero}: {resultado}")

    conn.close()


if __name__ == "__main__":

    padre_conn, hijo_conn = Pipe()

    # ⏱ Inicio del tiempo
    inicio = time.perf_counter()

    # Crear procesos
    p_lector = Process(target=leer_fichero, args=("numeros.txt", hijo_conn))
    p_sumador = Process(target=sumar_desde_pipe, args=(padre_conn,))

    p_lector.start()
    p_sumador.start()

    p_lector.join()
    p_sumador.join()

    # ⏱ Fin del tiempo
    fin = time.perf_counter()

    print(f"\nTiempo total de ejecución: {fin - inicio:.4f} segundos")
    print("Todos los procesos han terminado")

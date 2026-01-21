import multiprocessing
import random
import time


def generar_ip():
    return ".".join(str(random.randint(0, 255)) for _ in range(4))


def clase_ip(ip):
    primer_octeto = int(ip.split(".")[0])

    if 1 <= primer_octeto <= 126:
        return "A"
    elif 128 <= primer_octeto <= 191:
        return "B"
    elif 192 <= primer_octeto <= 223:
        return "C"
    else:
        return None


def proceso_1(cola_salida):
    for _ in range(10):
        ip = generar_ip()
        cola_salida.put(ip)
    cola_salida.put(None)  # Fin de datos


def proceso_2(cola_entrada, cola_salida):
    while True:
        ip = cola_entrada.get()
        if ip is None:
            cola_salida.put(None)
            break

        clase = clase_ip(ip)
        if clase in ("A", "B", "C"):
            cola_salida.put(ip)


def proceso_3(cola_entrada):
    while True:
        ip = cola_entrada.get()
        if ip is None:
            break

        clase = clase_ip(ip)
        print(f"IP: {ip} -> Clase {clase}")


if __name__ == "__main__":
    inicio = time.time()

    cola_1_2 = multiprocessing.Queue()
    cola_2_3 = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=proceso_1, args=(cola_1_2,))
    p2 = multiprocessing.Process(target=proceso_2, args=(cola_1_2, cola_2_3))
    p3 = multiprocessing.Process(target=proceso_3, args=(cola_2_3,))

    # Lanzar procesos en orden
    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

    fin = time.time()

    print(f"\nTiempo total de ejecución: {fin - inicio:.4f} segundos")

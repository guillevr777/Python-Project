from multiprocessing import Pool, cpu_count
import time

def sumar_hasta_n(n):
    """
    Suma todos los números desde 1 hasta n (incluido)
    """
    return sum(range(1, n + 1))


if __name__ == "__main__":

    # Valores de entrada
    valores = [5_000_000, 10_000_000, 15_000_000, 20_000_000]

    # Número de procesos a probar
    procesos_a_probar = [1, 2, 4, cpu_count()]

    print(f"Núcleos disponibles en el sistema: {cpu_count()}")

    for num_procesos in procesos_a_probar:
        print(f"\n--- Ejecutando con {num_procesos} procesos ---")

        inicio = time.perf_counter()

        with Pool(processes=num_procesos) as pool:
            resultados = pool.map(sumar_hasta_n, valores)

        fin = time.perf_counter()

        print("Resultados:", resultados)
        print(f"Tiempo con {num_procesos} procesos: {fin - inicio:.4f} segundos")

    print("\nTodos los procesos han terminado")

import multiprocessing
import time

# Función que suma todos los números entre a y b, incluyendo ambos
def sumar_rango(a, b):
    inicio = min(a, b)  # Para manejar si a > b
    fin = max(a, b)
    resultado = sum(range(inicio, fin + 1))
    print(f"Suma de {a} a {b}: {resultado}")
    return resultado

if __name__ == "__main__":
    # Lista de rangos para sumar
    rangos = [(1, 10), (5, 15), (20, 10), (100, 105)]
    
    # Guardamos el tiempo de inicio
    tiempo_inicio = time.time()
    
    # Crear un Pool de procesos
    with multiprocessing.Pool() as pool:
        # Usamos starmap para pasar múltiples argumentos
        resultados = pool.starmap(sumar_rango, rangos)
    
    # Tiempo de fin
    tiempo_fin = time.time()
    
    print("Todos los procesos han terminado.")
    print(f"Tiempo total de ejecución: {tiempo_fin - tiempo_inicio:.4f} segundos")

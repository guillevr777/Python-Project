def contarFrecuenciaPalabras(texto):
    # Convertir a minúsculas y separar en palabras
    palabras = texto.lower().split()
    
    # Crear un diccionario para contar frecuencias
    frecuencia = {}
    for palabra in palabras:

        if palabra:
            frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
    
    return frecuencia


# Programa principal
texto = input("Ingrese un texto: ")
resultado = contarFrecuenciaPalabras(texto)

print("Frecuencia de palabras:")
for palabra, cantidad in resultado.items():
    print(f"{palabra}: {cantidad}")

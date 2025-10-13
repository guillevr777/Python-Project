numeros = []
fichero = open('Ejercicios Ficheros/numeros.txt', 'r', encoding='utf8')
lineas = fichero.readlines()
for linea in lineas:
    numeros.append(int(linea))
fichero.close()
numeros.sort()
fichero = open('Ejercicios Ficheros/numeros_ordenados.txt', 'w', encoding='utf8')
for numero in numeros:
    fichero.write(f"{numero}\n")
fichero.close()
print(numeros)
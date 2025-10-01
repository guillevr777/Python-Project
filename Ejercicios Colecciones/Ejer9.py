import random

# Variables para almacenar la suma
suma = 0
#variable para recorrer la palabra por letra
letra = ''
#creacion del diccionario con las letras y su valor inicial 0
diccionario = {'a' : 0, 'b' : 0, 'c' : 0, 'd' : 0, 'e' : 0, 'f' : 0, 'g' : 0, 'h' : 0, 'i' : 0, 'j' : 0, 'k' : 0, 'l' : 0, 'm' : 0, 'n' : 0, 'o' : 0, 'p' : 0, 'q' : 0, 'r' : 0, 's' : 0, 't' : 0, 'u' : 0, 'v' : 0, 'w' : 0, 'x' : 0, 'y' : 0, 'z' : 0}

#asignacion de valores aleatorios a las letras del diccionario
for letra in diccionario:
    diccionario[letra] = random.randint(1, 26)

#pedir palabra al usuario
palabra = input("Introduce una palabra: ")
#variable para recorrer la palabra por letra
letra = ''

#suma de los valores de las letras que componen la palabra
for letra in palabra:
    suma += diccionario[letra]

#mostrar el diccionario y la suma de los valores de las letras
print(diccionario)
print(suma)
import random

#Creamos un variable entera contadora
cont = 0
#Creamos una lista de 10 elementos inicializados a 0
lista = [0]*10

#Bucle para rellenar la lista con numeros introducidos por teclado
while cont < 10:
    numero = int(input("Dime un numero"))
    lista [cont] = numero
    cont += 1

#Ordenamos la lista y la mostramos por consola
lista.sort()
print(lista)
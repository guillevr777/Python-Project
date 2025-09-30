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

#restablecemos el contador a 0 para volver a recorrer la lista
cont = 0

#Bucle para recorrer la lista y decir si es par o impar
while cont < 10 :
    if lista[cont] % 2 == 0 :
        print("El numero ", lista[cont], " es par")
    else :
        print("El numero ", lista[cont], " es impar")
    cont += 1

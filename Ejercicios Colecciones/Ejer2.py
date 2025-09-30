
import random

#Creamos un variable entera contadora
cont = 0
#Creamos una lista de 10 elementos inicializados a 0
lista = [0]*10
#Creamos una variable numero para guardar el numero mayor de la lista
mayor = 0
#Creamos una variable numero para guardar el numero menor de la lista
menor = 0
#Bucle para rellenar la lista con numeros introducidos por teclado
while cont < 10:
    numero = int(input("Dime un numero"))
    lista [cont] = numero
    cont += 1
    #Bucle para recorrer la lista y buscar el mayor y el menor
    if numero > mayor:
        mayor = numero
    elif numero < menor:
        menor = numero
#Mostramos el mayor, el menor y la lista
print("El mayor es: ", mayor)
print("El menor es: ", menor)   
print(lista)
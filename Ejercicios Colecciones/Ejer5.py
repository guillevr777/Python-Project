import random

#Creamos una lista de 100 elementos inicializados a 0
lista = [0] * 100
#Rellenamos la lista con numeros aleatorios entre 1 y 10
for i in range(100):
    lista[i] = random.randint(1, 10)

#Pedimos un numero por teclado y decimos cuantas veces aparece en la lista
numero = int(input("Dime un numero entre 1 y 10: "))
print("El numero ", numero, " aparece ", lista.count(numero), " veces")
print(lista)
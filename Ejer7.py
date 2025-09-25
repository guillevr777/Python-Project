numero = int(input('Dame un numero entero positivo'))
contador = 0
for secuencia in range (1,numero+1,1) :
    if numero % secuencia == 0 :
         contador += 1
if contador == 2 and numero >= 1 :
     print('Es un primo')
else :
     print('No lo es')
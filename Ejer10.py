def mostrarMayor (numero1, numero2) :
    if numero1 > numero2 :
      print('numero1 es mayor')
    elif numero2 > numero1 :
      print('numero1 es menor')
    else:
      print('Son iguales')


numero1 = int(input('Di un numero'))
numero2 = int(input('Di otro numero'))
mostrarMayor(numero1, numero2)
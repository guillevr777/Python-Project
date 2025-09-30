numero = int(input('Dime la anchura de la base de la piramide: '))
for i in range (1, numero + 1) :
    print(' ' * (numero - i) + '* ' * (i))
import random


numeroRandom = random.randint(0,101)    
intento = int(input('Dime numero'))
while numeroRandom != intento :
    if numeroRandom > intento :
        print('El numero es mas alto')
    else :
        print('El numero es mas bajo')
    intento = int(input('Di otro'))   
print('El numero era' , intento)
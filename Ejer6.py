numero = int(input('Dime el numero'))
resultado = 1
for escala in range (numero, 1, -1) :
    resultado *= escala
print(resultado)
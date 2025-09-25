def mostrarMayor (numero1, numero2) :
    opcion = int(input('Que opcion eliges\n1.Sumar\n2.Restar\n3.Multiplicar\n4.Dividir')) 
    match opcion :
        case 1 :
            resultado = numero1 + numero2
        case 2 :
            resultado = numero1 - numero2
        case 3 :
            resultado = numero1 * numero2
        case 4 :
            resultado = numero1 / numero2
    return resultado
resultado = int()
numero1 = int(input('Di un numero'))
numero2 = int(input('Di otro numero'))
resultado = mostrarMayor(numero1, numero2)
print(resultado)
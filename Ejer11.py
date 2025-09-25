def vocal (letra) :
    vocales = ['a','e','i','o','u']
    acierto = bool(False)
    if letra in vocales :
        acierto = True
    return acierto

letra = str(input('Di una letra').lower())
print(vocal(letra))
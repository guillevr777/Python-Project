diccionario = {'e': 'p', 'i':'v', 'k': 'i','m':'u','p':'m','q':'t','r':'e','s':'r','t':'k','u':'q','v':'s'}
frase = input("Introduce una frase: ")
nuevaFrase = ""
letra = ''

for letra in frase:
    if letra in diccionario:
        nuevaFrase += diccionario[letra]

    else:
        nuevaFrase += letra

print(nuevaFrase)
#Diccionario donde se guardaran las equivalencias para las letras del cifrado
diccionario = {'e': 'p', 'i':'v', 'k': 'i','m':'u','p':'m','q':'t','r':'e','s':'r','t':'k','u':'q','v':'s'}
#pedir frase al usuario
frase = input("Introduce una frase: ")
#variable para guardar la nueva frase cifrada
nuevaFrase = ""
#variable para recorrer la frase por letra
letra = ''

#recorrer la frase y sustituir las letras por su equivalencia en el diccionario
for letra in frase:
    if letra in diccionario:
        nuevaFrase += diccionario[letra]

    else:
        nuevaFrase += letra

#mostrar la frase cifrada
print(nuevaFrase)
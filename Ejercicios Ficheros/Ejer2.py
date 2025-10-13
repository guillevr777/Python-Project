fichero = open('Ejercicios Ficheros/ejer2.txt', 'w', encoding='utf8')
finalizar = True
while finalizar:
    texto = input("Introduce un texto (FIN para terminar): ")
    texto = texto.upper()
    if texto == "FIN":
        finalizar = False
    else:
        fichero.write(texto + "\n")
fichero.close()
fichero = open('Ejercicios Ficheros/ejer2.txt', 'r', encoding='utf8')
lineas = fichero.readlines()
for linea in lineas:
    print(linea)
fichero.close()
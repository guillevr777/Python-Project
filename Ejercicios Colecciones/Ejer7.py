
menu = 0
diccionario = {}
contacto = ""
telefono = 0
print("Menu de opciones")
print("1. Añadir palabra")
print("2. Eliminar palabra")
print("3. Mostrar palabras")
print("4. Salir")

while menu != 4:
    menu = int(input("Ingrese una opcion:"))
    match menu:
        case 1:
            contacto = input("Ingrese un contacto:")
            telefono = int(input("Ingrese un telefono:"))
            diccionario[contacto] = telefono
        case 2:
            contacto = input("Ingrese un contacto:")
            if (contacto in diccionario):
                del diccionario[contacto]
            else:
                print("El contacto no existe")
        case 3:
            for contacto in diccionario:
                print(contacto, diccionario[contacto])
#variable para elegir opcion del menu
menu = 0
#creacion del diccionario
diccionario = {}
#variables para añadir y eliminar contactos
contacto = ""
#variable para añadir telefono
telefono = 0
#menu de opciones
print("Menu de opciones")
print("1. Añadir palabra")
print("2. Eliminar palabra")
print("3. Mostrar palabras")
print("4. Salir")

#bucle para elegir opciones del menu
while menu != 4:
    menu = int(input("Ingrese una opcion:"))
    match menu:
        #Ingresar contacto y telefono
        case 1:
            contacto = input("Ingrese un contacto:")
            telefono = int(input("Ingrese un telefono:"))
            diccionario[contacto] = telefono
        #Eliminar contacto
        case 2:
            contacto = input("Ingrese un contacto:")
            if (contacto in diccionario):
                del diccionario[contacto]
            else:
                print("El contacto no existe")
        #Mostrar contactos
        case 3:
            for contacto in diccionario:
                print(contacto, diccionario[contacto])
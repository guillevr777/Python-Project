#veriable de control del menu
menu = 0
#creacion del diccionario
diccionario = {}
#variables para añadir y eliminar productos
producto = ""
#variable para añadir cantidad
cantidad = 0
#menu de opciones
print("Menu de opciones")
print("1. Añadir producto")
print("2. Mostrar productos")
print("3. Salir")

#bucle para elegir opciones del menu
while menu != 3:
    menu = int(input("Ingrese una opcion:"))
    match menu:
        case 1:
            contacto = input("Ingrese un producto:")
            diccionario[contacto] = diccionario.get(contacto, 0) + 1
        case 2:
            for contacto in diccionario:
                print(contacto, diccionario[contacto])
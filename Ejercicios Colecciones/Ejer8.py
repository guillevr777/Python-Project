menu = 0
diccionario = {}
producto = ""
cantidad = 0
print("Menu de opciones")
print("1. Añadir producto")
print("2. Mostrar productos")
print("3. Salir")

while menu != 3:
    menu = int(input("Ingrese una opcion:"))
    match menu:
        case 1:
            contacto = input("Ingrese un producto:")
            diccionario[contacto] = diccionario.get(contacto, 0) + 1
        case 2:
            for contacto in diccionario:
                print(contacto, diccionario[contacto])
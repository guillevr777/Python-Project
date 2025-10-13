fichero = open('Ejercicios Ficheros/alumnos.txt', 'w', encoding='utf8')
fichero.write(f"juan {22} 1.77\n")
fichero.write(f"Luis {21} 1.80\n")
fichero.write(f"Pedro {20} 1.73\n")
fichero.close()
fichero = open('Ejercicios Ficheros/alumnos.txt', 'r', encoding='utf8')
lineas = fichero.readlines()
mediaEdad = 0
mediaEstatura = 0
contador = 0
for linea in lineas:
    datos = linea.split()
    nombre = datos[0]
    edad = int(datos[1])
    altura = float(datos[2])
    print(f"Nombre: {nombre}, Edad: {edad}, Altura: {altura}")
    mediaEstatura += altura
    mediaEdad += edad
    contador += 1
mediaEdad = mediaEdad / contador
mediaEstatura = mediaEstatura / contador
print(f"La media de estaturas es: {mediaEstatura}")
print(f"La media de edades es: {mediaEdad}")
fichero.close()
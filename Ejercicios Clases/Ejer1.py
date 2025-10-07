class CuentaCorriente:
    def __init__(self, dni, nombre, saldo):
        self.dni = dni
        self.nombre = ""
        self.saldo = saldo

    def __init__(self, dni, saldo):
        self.dni = dni
        self.nombre = ""
        self.saldo = saldo

    def ingresarDinero(dinero):
        saldo += dinero

    def retirarDinero(dinero):
        if saldo >= dinero:
            saldo -= dinero
        else:
            print("No hay suficiente saldo")

    def __str__(self):
        cadena = "DNI: " + self.dni + " Nombre: " + self.nombre + " Saldo: " + str(self.saldo)
        return cadena

    def __eq__(self, objeto):
        iguales = False
        if self.dni == objeto.dni:
            iguales = True
        return iguales

    def __lt__(self, objeto):
        menor = False
        if self.saldo < objeto.saldo:
            menor = True
        return menor
    
obj = CuentaCorriente("12345678A", "Juan Perez", 1000)
obj2 = CuentaCorriente("87654321B", 500)

obj.ingresarDinero(200)
obj.retirarDinero(100)
print(obj.__lt__(obj2))
print(obj.__eq__(obj2))

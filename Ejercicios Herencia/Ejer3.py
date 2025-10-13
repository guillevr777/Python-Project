class Producto :
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def getNombre(self):
        return self.nombre

    def getPrecio(self):
        return self.precio
    
    def calcular(self, cantidad):
        return self.precio * cantidad
    
    def __str__(self):
        return f"Producto: {self.nombre}, Precio: {self.precio}€"
    
class Perecedero(Producto):
    def __init__(self, nombre, precio, fechaCaducidad):
        super().__init__(nombre, precio)
        self.fechaCaducidad = fechaCaducidad

    def getFechaCaducidad(self):
        return self.fechaCaducidad
    
    def calcular(self, cantidad):
        precio = 0

        if self.fechaCaducidad == 1:
            precio = (self.precio * cantidad) / 4
        elif self.fechaCaducidad == 2:
            precio = (self.precio * cantidad) / 3
        elif self.fechaCaducidad == 3:
            precio = (self.precio * cantidad) / 2

        return precio
    
    def __str__(self):
        return f"Perecedero: {self.nombre}, Precio: {self.precio}€, Fecha de caducidad: {self.fechaCaducidad}"
    
class NoPerecedero(Producto):
    def __init__(self, nombre, precio):
        super().__init__(nombre, precio)
    
    def calcular(self, cantidad):
        return super().calcular(cantidad)
    
    def __str__(self):
        return f"No Perecedero: {self.nombre}, Precio: {self.precio}€"
class Articulo:

    IVA = 1.21

    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def getPVP(self):
        return self.precio * self.IVA
    
    def getPVPDescuento(self, descuento):
        
        self.precio = self.precio * descuento

        return self.precio
    
    def vender(self, vendido):
        sePudo = False
        if self.sotck > vendido:
          self.stock -= vendido
          sePudo = True
        return sePudo
    
    def almacenar(self, cantidad):
        sePudo = False
        if cantidad > 0:
            self.stock += cantidad
            sePudo = True
        return sePudo
    
    def __str__(self):
        return f"Cantidad: {self.stock} Nombre: {self.nombre} Precio: {self.precio}"
        
    def __eq__(self, value):
        iguales = False
        if self.nombre == value.nombre:
            iguales = True
        return iguales
        
    def __lt__(self, value):
        return self.nombre < value.nombre
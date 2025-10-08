class Animal:
    def __init__(self, nombre, nPatas):
        self.nombre = nombre
        self.nPatas = nPatas
    
    def habla():
        return ""
    
    def __str__(self):
        return f"Me llamo {self.nombre}, tengo {self.nPatas} patas y sueno así: {self.habla()}"
    
class Gato(Animal):
    def __init__(self, nombre, nPatas):
        super.__init__(nombre, nPatas)

    def habla():
            return "Miau"
    
    def __str__(self):
        return f"Soy un gato, Me llamo {self.nombre}, tengo {self.nPatas} patas y sueno así: {self.habla()}"
    
class Perro(Animal):
    def __init__(self, nombre, nPatas):
        super.__init__(nombre, nPatas)

    def habla():
            return "Guau"
    
    def __str__(self):
        return f"Soy un Perro, Me llamo {self.nombre}, tengo {self.nPatas} patas y sueno así: {self.habla()}"
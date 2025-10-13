class Empleado:

    def __init__(self, nombre):
        self.nombre = nombre

    def setNombre(self, nombre):

        self.nombre = nombre

    def getNombre(self):

        return self.nombre

    def __str__(self):
        return f"Empleado {self.nombre}"

class Operario(Empleado):

    def __init__(self, nombre):
        super().__init__(nombre)

    def setNombre(self, nombre):

        self.nombre = nombre

    def getNombre(self):

        return self.nombre
    
    def __str__(self):
        return f"-> Operario "

class Directivo(Empleado):

    def __init__(self, nombre):
        super().__init__(nombre)
    
    def setNombre(self, nombre):

        self.nombre = nombre

    def getNombre(self):

        return self.nombre
    
    def __str__(self):
        return f"-> Directivo "

class Oficial(Operario):

    def __init__(self, nombre):
        super().__init__(nombre)
    
    def setNombre(self, nombre):

        self.nombre = nombre

    def getNombre(self):

        return self.nombre
    
    def __str__(self):
        return f"-> Oficial "

class Tecnico(Operario):

    def __init__(self, nombre):
        super().__init__(nombre)
    
    def setNombre(self, nombre):

        self.nombre = nombre

    def getNombre(self):

        return self.nombre
    
    def __str__(self):
        return f"-> Técnico "
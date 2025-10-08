class Empleado:

    def __init__(self, nombre):
        self.nombre = nombre

    def setNombre(self, nombre):

        self.nombre = nombre

    def getNombre(self):

        return self.nombre

class Operario(Empleado):

    def __init__(self, nombre):
        super().__init__(nombre)

    def setNombre(self, nombre):

        self.nombre = nombre

    def getNombre(self):

        return self.nombre

class Directivo(Empleado):

    def __init__(self, nombre):
        super().__init__(nombre)
    
    def setNombre(self, nombre):

        self.nombre = nombre

    def getNombre(self):

        return self.nombre

class Oficial(Operario):

    def __init__(self, nombre):
        super().__init__(nombre)
    
    def setNombre(self, nombre):

        self.nombre = nombre

    def getNombre(self):

        return self.nombre

class Tecnico(Operario):

    def __init__(self, nombre):
        super().__init__(nombre)
    
    def setNombre(self, nombre):

        self.nombre = nombre

    def getNombre(self):

        return self.nombre
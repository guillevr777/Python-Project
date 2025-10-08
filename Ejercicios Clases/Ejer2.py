class Libro :

    libros = []

    def __init__ (self, titulo, autor, cantidad, prestados) :
        self.titulo = titulo
        self.autor = autor
        self.cantidad = cantidad
        self.prestados = prestados

    def prestamo () :
        prestó: False

        if (cantidad > prestados and cantidad > 0) :
            prestados += 1
            cantidad -= 1
            prestó = True

        return prestó
    
    def devolucion () :
        devolvió = False

        if (prestados > 0) :
            prestados -= 1
            cantidad += 1
            devolvió = True

        return devolvió

    def __str__(self):
        return "Nombre:" + self.titulo + " Autor:" + self.autor + " Cantidad:" + self.cantidad + " Prestados:" + self.prestados
    
    def __eq__(self, value):
        correcto = False

        if (self.titulo == value.titulo) :
            correcto = True
        
        return correcto
    
    def __lt__(self, value) :
        correcto = False

        if (self.autor < value.autor) :
            correcto = True

        return correcto
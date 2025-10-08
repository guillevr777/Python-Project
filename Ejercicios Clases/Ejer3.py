class Punto :
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def setXY(self, x, y) :
        if x is not None :
            self.x = x
        if y is not None :
            self.y = y

    def desplaza (self, dx, dy):
        if (dx is not None):
            self.x += dx
        if (dy is not None):
            self.y += dy

    def devolverDistancia (self, value):
        if self.x > value.x:
            resultadoX = self.x - value.x
            resultadoY = self.y - value.y
        return "("+ resultadoX + "," + resultadoY + ")"

    def __str__(self):
        return "'(" + self.x + " + " + self.y + ")'"
import random
from Nave import Nave


class Tablero:
    def __init__(self):
        self.tablero: list[list[Nave | tuple]] = [
            [("Agua", 0)] * 10 for _ in range(10)]

    def colocar_nave(self, nave: Nave):

        while True:
            fila = random.randint(0, 9)
            col = random.randint(0, 9)
            if self.tablero[fila][col] == ("Agua", 0):
                self.tablero[fila][col] = nave
                break

    def gestionar_disparo(self, x, y):
        celda = self.tablero[x][y]
        if isinstance(celda, Nave):
            return celda.recibir_disparo()
        else:
            return "Agua"

    def __str__(self):
        resultado = ""
        for fila in self.tablero:
            for celda in fila:
                resultado += str(celda) + "  "
            resultado += "\n"
        return resultado

import random
from Nave import Nave


class Tablero:
    """
    Clase que crea un tablero nuevo, usando una matriz 10 x 10, ademas coloca naves en sitios random (2 de cada una)
    """

    def __init__(self):
        self.tablero: list[list[Nave | tuple]] = [
            [("Agua", 0)] * 10 for _ in range(10)]

    def colocar_nave(self, nave: Nave):
        # Las naves deben tener un tamaño real no solo referencial
        while True:
            direccion = random.choice(["H", "V"])
            if direccion == "H":

                fila = random.randint(0, 9)
                col = random.randint(0, 10 - nave.vida)
                celdas = []
                for i in range(nave.vida):
                    celdas.append((fila, col+i))
            else:
                fila = random.randint(0, 10 - nave.vida)
                col = random.randint(0, 9)
                celdas = []
                for i in range(nave.vida):
                    celdas.append((fila + i, col))
            libre = True
            for f, c in celdas:
                if self.tablero[f][c] != ("Agua", 0):
                    libre = False
                    break
            if libre:
                for f, c in celdas:
                    self.tablero[f][c] = nave
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

import random
from Nave import Nave
from Casilla import Casilla


class Tablero:
    """
    Clase que crea un tablero nuevo, usando una matriz 10 x 10 de objetos Casilla.
    Coloca naves en posiciones aleatorias y gestiona los disparos.
    """

    def __init__(self):
        self.tablero: list[list[Casilla]] = [
            [Casilla() for _ in range(10)] for _ in range(10)]

    def colocar_nave(self, nave: Nave):
        while True:
            fila = random.randint(0, 9)
            col = random.randint(0, 9)
            if self.tablero[fila][col].nave is None:
                self.tablero[fila][col].nave = nave
                break

    def gestionar_disparo(self, x, y):
        casilla = self.tablero[x][y]

        if casilla.visitada:
            return "Ya disparado"

        casilla.visitada = True

        if casilla.nave is None:
            return "Agua"
        else:
            return casilla.nave.recibir_disparo()

    def __str__(self):
        resultado = ""
        for fila in self.tablero:
            for casilla in fila:
                if casilla.nave is not None:
                    resultado += str(casilla.nave) + "  "
                else:
                    resultado += "Agua  "
            resultado += "\n"
        return resultado

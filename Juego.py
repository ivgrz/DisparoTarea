from Nave import Nave
from Tablero import Tablero


class Juego:
    def __init__(self):
        self.tablero = Tablero()
        self.naves = []
        self.inicializar_naves()

    def inicializar_naves(self):
        datos = [
            ("Enterprise", "portaaviones", 5),
            ("Bismarck", "fragata", 3),
            ("Prince of Wales", "fragata", 3),
            ("Graf Spee", "fragata", 3),
            ("U-47", "submarino", 1),
            ("U-96", "submarino", 1),
            ("U-505", "submarino", 1),
            ("U-534", "submarino", 1),
        ]
        for nombre, tipo, tamano in datos:
            nave = Nave(nombre, tipo, tamano)
            self.naves.append(nave)
            self.tablero.colocar_nave(nave)

    def lanzar_ataque(self, x, y):
        return self.tablero.gestionar_disparo(x, y)


if __name__ == "__main__":

    juego = Juego()

    while True:
        print("---BIENVENIDO AL JUEGO---\n")
        print("1. Ver Tablero\n")
        print("2. Lanzar ataque\n")
        print("3. Salir")
        opcion = input("Elige una opcion: ")

        match opcion:
            case "1":
                print(juego.tablero)
            case "2":
                x = int(input("Elige una fila: "))
                y = int(input("Elige una columna: "))
                print(juego.lanzar_ataque(x, y))
            case "3":
                print("Saliendo...")
                break

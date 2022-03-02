#! /user/bin/env python
import math


class Punto:
    """Representa un punto en sus cordenadas geométricas bidimensionales."""

    def __init__(self, x=0, y=0) -> None:
        """Metodo especial de para iniciar los objetos"""
        self.mover(x, y)

    def mover(self, x, y):
        """Mueve el pnto a una nueva localizacion bidimencional."""
        self.x = x
        self.y = y

    def reiniciar(self):
        """Reinicia el punto al origen geometrico 0,0"""
        self.mover(0, 0)

    def calcular_distancia(self, otro_punto) -> float:
        """Calcula la distancia de este punto a un segunfo punto pasado como parámetro
        Se utiliza el teorema de pitagoras para calcular la distancia.
        La distancia se devuelve como float.
        """
        return math.sqrt((self.x - otro_punto.x) ** 2 + (self.y - otro_punto.y) ** 2)


def main():
    punto = Punto(4, 2)
    punto2 = Punto(2)
    punto3 = Punto()
    # punto.x = 3
    pass


if __name__ == "__main__":
    main()

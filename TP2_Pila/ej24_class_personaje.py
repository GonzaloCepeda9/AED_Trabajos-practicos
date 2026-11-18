class Personaje:
    def __init__(self, nombre: str, cantidad_peliculas: int):
        self.nombre = nombre
        self.cantidad_peliculas = cantidad_peliculas

    def __str__(self):
        return f'{self.nombre} | {self.cantidad_peliculas}'


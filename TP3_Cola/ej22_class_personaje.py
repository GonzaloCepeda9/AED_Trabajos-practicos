class Personaje:
    def __init__(self, nombre_personaje: str, nombre_superheroe: int, genero):
        self.nombre_personaje = nombre_personaje
        self.nombre_superheroe = nombre_superheroe
        self.genero = genero

    def __str__(self):
        return f'{self.nombre_personaje} | {self.nombre_superheroe} | {self.genero}'
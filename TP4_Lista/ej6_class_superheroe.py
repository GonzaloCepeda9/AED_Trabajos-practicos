class Superheroe:

    def __init__(self, nombre: str, anio_aparicion: int, casa_comic: str, biografia: str):
        self.nombre = nombre
        self.anio_aparicion = anio_aparicion
        self.casa_comic = casa_comic
        self.biografia = biografia

    def __str__(self):
        return f'Nombre: {self.nombre} | Año de aparición: {self.anio_aparicion} | Casa de comic: {self.casa_comic} | Biografía: {self.biografia}'
from TDA_list import List

class Entrenador_Pokemon:
    def __init__(self, nombre: str, torneos_ganados: int, batallas_perdidas: int, batallas_ganadas: int):
        self.nombre = nombre
        self.torneos_ganados = torneos_ganados
        self.batallas_perdidas = batallas_perdidas
        self.batallas_ganadas = batallas_ganadas
        self.lista_pokemons = List()

    def __str__(self):
        return f'{self.nombre} | Torneos ganados: {self.torneos_ganados} | Batallas ganadas: {self.batallas_ganadas} | Batallas perdidas: {self.batallas_perdidas}'
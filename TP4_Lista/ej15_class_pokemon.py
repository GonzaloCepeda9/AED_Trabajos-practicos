class Pokemon:
    def __init__(self, nombre: str, nivel: int, tipo: str, subtipo: str):
        self.nombre = nombre
        self.nivel = nivel
        self.tipo = tipo
        self.subtipo = subtipo

    def __str__(self):
        return f'{self.nombre} | Nivel: {self.nivel} | Tipo: {self.tipo} | Subtipo: {self.subtipo}'
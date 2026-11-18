class Notification:
    def __init__(self, app_emisora: str, hora: str, mensaje: str):
        self.app_emisora = app_emisora
        self.hora = hora
        self.mensaje = mensaje

    def __str__(self):
        return f'App: {self.app_emisora} | Hora: {self.hora} | Mensaje: {self.mensaje}'
# 10. Notificaciones
'''
Dada una cola con las notificaciones de las aplicaciones de redes sociales de un Smartphone, de las cual se cuenta con la hora de la notificación, la aplicación que la emitió y el mensaje, resolver las siguientes actividades:
a. escribir una función que elimine de la cola todas las notificaciones de Facebook;
b. escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya la palabra 'Python', sin perder datos en la cola;
c. utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las 11:43 y las 15:57, y determinar cuántas son.
'''

from ED_queue import Queue
from ED_stack import Stack
from ej10_class_notificacion import Notification

# a. escribir una función que elimine de la cola todas las notificaciones de Facebook;
def eliminar_por_app(queue: Queue, app: str):
    for _ in range(queue.size()):
        notif_frente = queue.on_front()
        if notif_frente.app_emisora == app:
            queue.attention()
        else:
            queue.move_to_end()
    return queue

# b. escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya la palabra 'Python', sin perder datos en la cola;
def mostrar_notif_especificas(queue: Queue, app: str, palabra: str):
    queue_aux = Queue()
    for _ in range(queue.size()):
        notif_frente = queue.on_front()
        if notif_frente.app_emisora == app and palabra in notif_frente.mensaje:
            queue_aux.arrive(notif_frente)
        queue.move_to_end()
    return queue, queue_aux

# c. utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las 11:43 y las 15:57, y determinar cuántas son.
def determinar_notificaciones(queue: Queue, hora_inicio: str, hora_final: str):
    stack_aux = Stack()
    cantidad: int = 0
    for _ in range(queue.size()):
        notif_frente = queue.on_front()
        if notif_frente.hora >= hora_inicio and notif_frente.hora <= hora_final:
            stack_aux.push(notif_frente)
            cantidad += 1
        queue.move_to_end()
    return stack_aux, cantidad

#################################################  Ejecución de pruebas del enunciado  #################################################
queue_notification = Queue()
stack_aux_b = Stack()
stack_aux_c = Stack()

queue_notification.arrive(Notification('Twitter', '11:45', 'Aprendiendo Python con Walter.'))
queue_notification.arrive(Notification('Instagram', '12:15', 'Nuevo me gusta a tu foto.'))
queue_notification.arrive(Notification('Facebook', '13:30', 'Tienes una solicitud de amistad.'))
queue_notification.arrive(Notification('Twitter', '14:20', 'Curso de Python recomendado.'))
queue_notification.arrive(Notification('Twitter', '15:30', 'Nuevo tweet de Python.org.'))
queue_notification.arrive(Notification('Twitter', '15:55', 'Novedades sobre Python.'))
queue_notification.arrive(Notification('WhatsApp', '16:10', 'Mensaje de grupo familiar.'))
queue_notification.arrive(Notification('Facebook', '14:45', 'Otro tweet sobre programación.'))

print('\n---------------------------------------------- Cola original de notificaciones -----------------------------------------------')
print('Cola original: ')
queue_notification.show()

# a. escribir una función que elimine de la cola todas las notificaciones de Facebook;
print('\n-------------------------------------------- Eliminación de notificaciones de app --------------------------------------------')
# aplicacion1 = input('Ingrese el nombre de la app de la cuál desea eliminar las notificaciones: ')  # Utilizar en caso que se quiera solicitar al usuario
aplicacion1 = 'Facebook'
eliminar_por_app(queue_notification, aplicacion1)
print(f'Nombre de la app de la cuál se eliminarán las notificaciones: {aplicacion1}. \nCola actualizada: ')
queue_notification.show()

# b. escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya la palabra 'Python', sin perder datos en la cola;
print('\n----------------------------------- Muestra de notificaciones según app y palabra incluida -----------------------------------')
# aplicacion2 = input('Ingrese el nombre de la app de la cuál desea mostrar las notificaciones: ')  # Utilizar en caso que se quiera solicitar al usuario
# palabra_incluida = input('Ingrese la palabra que debe tener incluida: ') # Utilizar en caso que se quiera solicitar al usuario
aplicacion2 = 'Twitter'
palabra_incluida = 'Python'
queue_notification, stack_aux_b = mostrar_notif_especificas(queue_notification, aplicacion2, palabra_incluida)
print(f'App de la cuál se mostrarán las notificaciones: {aplicacion2}. \nPalabra que debe incluir: {palabra_incluida}.')
if not stack_aux_b.is_empty():
    print('Cola con notificaciones solicitadas: ')
    stack_aux_b.show()
else:
    print(f'No se encontró ninguna notificación con los datos proporcionados.')

# c. utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las 11:43 y las 15:57, y determinar cuántas son.
print('\n------------------------------------- Determinación de notificaciones en hora específica -------------------------------------')
# hora_inicio = input('Ingrese hora de inicio: ')  # Utilizar en caso que se quiera solicitar al usuario
# hora_final = input('Ingrese la hora final: ') # Utilizar en caso que se quiera solicitar al usuario
hora_inicio = '11:43'
hora_final = '15:47'
stack_aux_c, cantidad = determinar_notificaciones(queue_notification, hora_inicio, hora_final)
print(f'Pila con notificaciones almacenadas: ')
stack_aux_c.show()
print(f'\nTotal de notificaciones producidas entre las {hora_inicio} y {hora_final}: {cantidad}')
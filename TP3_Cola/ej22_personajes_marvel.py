# 22. Personajes de Marvel Cinematic Universe (MCU)
"""
Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se conoce el nombre del personaje, el nombre del superhéroe y su género (Masculino M y Femenino F) por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Romanoff, Black Widow, F}, etc., desarrollar un algoritmo que resuelva las siguientes actividades:
a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
b. mostrar los nombres de los superhéroes femeninos;
c. mostrar los nombres de los personajes masculinos;
d. determinar el nombre del superhéroe del personaje Scott Lang;
e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan con la letra S;
f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre de superhéroes.
"""

from ED_queue import Queue
from ej22_class_personaje import Personaje

# a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
def determinar_nombre_personaje(queue: Queue, superheroe: str):
    nombre = None
    for _ in range(queue.size()):
        personaje_frente = queue.on_front()
        if personaje_frente.nombre_superheroe == superheroe:
            nombre = personaje_frente.nombre_personaje
        queue.move_to_end()
    return nombre

# b. mostrar los nombre de los superhéroes femeninos;
def mostrar_por_genero(queue: Queue, genero: str):
    queue_aux = Queue()
    for _ in range(queue.size()):
        personaje_frente = queue.on_front()
        if personaje_frente.genero == genero:
            queue_aux.arrive(personaje_frente)
        queue.move_to_end()
    return queue_aux

# d. determinar el nombre del superhéroe del personaje Scott Lang;
def determinar_nombre_superheroe(queue: Queue, personaje: str):
    nombre = None
    for _ in range(queue.size()):
        personaje_frente = queue.on_front()
        if personaje_frente.nombre_personaje == personaje:
            nombre = personaje_frente.nombre_superheroe
        queue.move_to_end()
    return nombre

# e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan con la letra S;
def buscar_por_inicial(queue: Queue, letra: str):
    queue_aux = Queue()
    for _ in range(queue.size()):
        personaje_frente = queue.on_front()
        if personaje_frente.nombre_personaje[0] == letra or personaje_frente.nombre_superheroe[0] == letra:
            queue_aux.arrive(personaje_frente)
        queue.move_to_end()
    return queue_aux

# f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre de superhéroes.
def buscar_por_nombre(queue: Queue, personaje: str):
    buscado: str = None
    for _ in range(queue.size()):
        personaje_frente = queue.on_front()
        if personaje_frente.nombre_personaje == personaje:
            buscado = personaje_frente.nombre_superheroe
        queue.move_to_end()
    return buscado

#################################################  Ejecución de pruebas del enunciado  #################################################
queue_mcu = Queue()
queue_mcu.arrive(Personaje("Tony Stark", "Iron Man", "M"))
queue_mcu.arrive(Personaje("Steve Rogers", "Capitán América", "M"))
queue_mcu.arrive(Personaje("Thor Odinson", "Thor", "M"))
queue_mcu.arrive(Personaje("Natasha Romanoff", "Black Widow", "F"))
queue_mcu.arrive(Personaje("Clint Barton", "Hawkeye", "M"))
queue_mcu.arrive(Personaje("Bruce Banner", "Hulk", "M"))
queue_mcu.arrive(Personaje("Nick Fury", "Nick Fury", "M"))
queue_mcu.arrive(Personaje("Loki Laufeyson", "Loki", "M"))
queue_mcu.arrive(Personaje("Peter Parker", "Spider-Man", "M"))
queue_mcu.arrive(Personaje("Stephen Strange", "Doctor Strange", "M"))
queue_mcu.arrive(Personaje("T'Challa", "Black Panther", "M"))
queue_mcu.arrive(Personaje("Scott Lang", "Ant-Man", "M"))
queue_mcu.arrive(Personaje("Wanda Maximoff", "Scarlet Witch", "F"))
queue_mcu.arrive(Personaje("Sam Wilson", "Falcon", "M"))
queue_mcu.arrive(Personaje("Bucky Barnes", "Winter Soldier", "M"))
queue_mcu.arrive(Personaje("James Rhodes", "War Machine", "M"))
queue_mcu.arrive(Personaje("Carol Danvers", "Captain Marvel", "F"))
queue_mcu.arrive(Personaje("Gamora", "Gamora", "F"))
queue_mcu.arrive(Personaje("Rocket Raccoon", "Rocket", "M"))
queue_mcu.arrive(Personaje("Thanos", "Thanos", "M"))

# a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
print('\n------------------------------------ Determinación del nombre de personaje del superhéroe ------------------------------------')
superheroe_buscado = 'Captain Marvel'
nombre_personaje = determinar_nombre_personaje(queue_mcu, superheroe_buscado)
if nombre_personaje:
    print(f'Nombre del personaje de él/la superheroe "{superheroe_buscado}": {nombre_personaje}.')
else:
    print(f'El superheroe "{superheroe_buscado}" no se encuentra en la lista.')

# b. mostrar los nombre de los superhéroes femeninos;
print('\n------------------------------------------- Muestra de superheroes según su género -------------------------------------------')
genero = 'F'
queue_genero = mostrar_por_genero(queue_mcu, genero)
if genero == 'F':
    print(f'Nombre de personajes de género Femenino: ')
    queue_genero.show()
elif genero == 'M':
    print(f'Nombre de personajes de género Masculino: ')
    queue_genero.show()
else:
    print(f'No se encontró ningún personaje de género {genero}.')

# c. mostrar los nombres de los personajes masculinos;
genero = 'M'
queue_genero = mostrar_por_genero(queue_mcu, genero)
if genero == 'F':
    print(f'\nNombre de personajes de género Femenino: ')
    queue_genero.show()
elif genero == 'M':
    print(f'\nNombre de personajes de género Masculino: ')
    queue_genero.show()
else:
    print(f'\nNo se encontró ningún personaje de género correspondiente a la letra {genero}.')

# d. determinar el nombre del superhéroe del personaje Scott Lang;
print('\n------------------------------------ Determinación del nombre de superhéroe del personaje ------------------------------------')
personaje_buscado = 'Scott Lang'
nombre_superheroe = determinar_nombre_superheroe(queue_mcu, personaje_buscado)
if nombre_superheroe:
    print(f'Nombre de superhéroe de él/la personaje "{personaje_buscado}": {nombre_superheroe}.')
else:
    print(f'El personaje "{personaje_buscado}" no se encuentra en la lista.')

# e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan con la letra S;
print('\n------------------------------- Muestra de datos de superhéroes o personajes según su inicial --------------------------------')
letra = 'S'
queue_aux_e = buscar_por_inicial(queue_mcu, letra)
if not queue_aux_e.is_empty():
    print(f'Personajes cuyo nombre comienza con la letra "{letra}": ')
    queue_aux_e.show()
else:
    print(f'No se encontró ningún personaje cuyo nombre comience con la letra {letra}.')

# f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre de superhéroes.
print('\n------------------------------- Búsqueda de personaje y determinación de nombre de superhéroe --------------------------------')
personaje = 'Carol Danvers'
buscado = buscar_por_nombre(queue_mcu, personaje)
if buscado:
    print(f'El personaje "{personaje}" se encuentra en la Cola. Su nombre de supereroe es: {buscado}.')
else:
    print(f'El personaje "{personaje}" no se encuentra en la Cola.')
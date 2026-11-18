"""
24. Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones necesarias para resolver las siguientes actividades:
    a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición uno la cima de la pila;
    b. determinar los personajes que participaron en más de 5 películas de la saga, además indicar la cantidad de películas en la que aparece;
    c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
    d. mostrar todos los personajes cuyos nombre empiezan con C, D y G
"""

from stack import Stack
from ej24_class_personaje import Personaje

pila_personajes = Stack()

pila_personajes.push(Personaje("Iron Man", 10))
pila_personajes.push(Personaje("Captain America (Capitán América)", 11))
pila_personajes.push(Personaje("Thor", 8))
pila_personajes.push(Personaje("Black Widow (Viuda Negra)", 9))
pila_personajes.push(Personaje("Hawkeye (Ojo de Halcón)", 6))
pila_personajes.push(Personaje("Hulk", 8))
pila_personajes.push(Personaje("Nick Fury (Nick Furia)", 11))
pila_personajes.push(Personaje("Loki", 6))
pila_personajes.push(Personaje("Spider-Man", 7))
pila_personajes.push(Personaje("Doctor Strange", 5))
pila_personajes.push(Personaje("Black Panther (Pantera Negra)", 5))
pila_personajes.push(Personaje("Ant-Man (Hombre Hormiga)", 5))
pila_personajes.push(Personaje("Scarlet Witch (Bruja Escarlata)", 7))
pila_personajes.push(Personaje("Falcon (Halcón)", 7))
pila_personajes.push(Personaje("Groot", 5))
pila_personajes.push(Personaje("Winter Soldier (Soldado del Invierno)", 7))
pila_personajes.push(Personaje("War Machine (Máquina de Guerra)", 7))
pila_personajes.push(Personaje("Captain Marvel (Capitana Marvel)", 4))
pila_personajes.push(Personaje("Gamora", 5))
pila_personajes.push(Personaje("Rocket Raccoon", 5))
pila_personajes.push(Personaje("Thanos", 8))

# a. Determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición uno la cima de la pila;

def posicion_personaje(pila: Stack, personaje_buscado: str):

    pila_aux = Stack()
    posicion = None

    for i in range(pila.size()):
        personaje = pila.pop()
        pila_aux.push(personaje)

        if personaje.nombre == personaje_buscado:
            posicion = i+1
        
    # Restaurar la pila original:
    while pila_aux.size() > 0:
        pila.push(pila_aux.pop())

    return posicion

# b. Determinar los personajes que participaron en más de 5 películas de la saga, además indicar la cantidad de películas en la que aparece;

def personajes_mayor_participacion(pila: Stack, cantidad: int):

    pila_aux = Stack()
    pj_mayor_participacion = {}

    while pila.size() > 0:
        personaje = pila.pop()
        pila_aux.push(personaje)

        if personaje.cantidad_peliculas > cantidad:
            pj_mayor_participacion[personaje.nombre] = personaje.cantidad_peliculas
        
    # Restaurar la pila original:
    while pila_aux.size() > 0:
        pila.push(pila_aux.pop())
    
    return pj_mayor_participacion

# c. Determinar en cuantas películas participo la Viuda Negra (Black Widow);

def participacion_individual(pila: Stack, buscado: str):
    
    pila_aux = Stack()
    cantidad = None

    while pila.size() > 0:
        personaje = pila.pop()
        pila_aux.push(personaje)

        if personaje.nombre == buscado:
            cantidad = personaje.cantidad_peliculas

     # Restaurar la pila original:
    while pila_aux.size() > 0:
        pila.push(pila_aux.pop())   
    
    return cantidad

# d. Mostrar todos los personajes cuyos nombre empiezan con C, D y G

def buscar_por_inicial(pila: Stack, letra_inicial: str):

    pila_aux = Stack()
    personajes = []

    while pila.size() > 0:
        personaje = pila.pop()
        pila_aux.push(personaje)

        if personaje.nombre[0] == letra_inicial:
            personajes.append(personaje.nombre)

      # Restaurar la pila original:
    while pila_aux.size() > 0:
        pila.push(pila_aux.pop())
    
    return personajes

print('\n-------------------------------------------------- a. Posición del personaje -------------------------------------------------')
personaje_1 = 'Rocket Raccoon'
posicion_pj1 = posicion_personaje(pila_personajes, personaje_1)
if posicion_pj1 is not None:
    print(f'El personaje {personaje_1} se encuentra en la posición {posicion_pj1}.')
else:
    print('El personaje no se encuentra en la lista.')

personaje_2 = 'Groot'
posicion_pj2 = posicion_personaje(pila_personajes, personaje_2)
if posicion_pj2 is not None:
    print(f'El personaje {personaje_2} se encuentra en la posición {posicion_pj2}.')
else:
    print('El personaje no se encuentra en la lista.')



print('\n------------------------------------- b. Personajes con mayor participación en películas -------------------------------------')
cantidad = 5
participacion_peliculas = personajes_mayor_participacion(pila_personajes, cantidad)
if participacion_peliculas:
    for nombre, cantidad in participacion_peliculas.items():
        print(f'El personaje {nombre} participó en {cantidad} películas.')
else:
    print(f'Ningún personaje participó en más de {cantidad} películas.')

print('\n----------------------------------------------- c. Participación del personaje -----------------------------------------------')
pj_buscado = 'Black Widow (Viuda Negra)'
cantidad_peliculas = participacion_individual(pila_personajes, pj_buscado)
if cantidad_peliculas is not None:
    print(f'El personaje {pj_buscado} participó en {cantidad_peliculas} película/s.')
else:
    print('El personaje no participó en ninguna de las películas de la pila.')

print('\n---------------------------------------------- d. Buscar personajes por inicial ----------------------------------------------')
inicial_1 = 'C'
personajes_1 = buscar_por_inicial(pila_personajes, inicial_1)
if personajes_1:
    print(f'Los personajes cuyos nombres comienzan con la inicial {inicial_1} son: {personajes_1}.')
else:
    print(f'No se encontraron personajes cuyos nombres comiencen con la inicial {inicial_1}.')

inicial_2 = 'D'
personajes_2 = buscar_por_inicial(pila_personajes, inicial_2)
if personajes_2:
    print(f'Los personajes cuyos nombres comienza con la inicial {inicial_2} son: {personajes_2}.')
else:
    print(f'No se encontraron personajes cuyos nombres comience con la inicial {inicial_2}.')

inicial_3 = 'G' 
personajes_3 = buscar_por_inicial(pila_personajes, inicial_3)
if personajes_3:
    print(f'Los personajes cuyos nombres comienza con la inicial {inicial_3} son: {personajes_3}.')
else:
    print(f'No se encontraron personajes cuyos nombres comience con la inicial {inicial_3}.')
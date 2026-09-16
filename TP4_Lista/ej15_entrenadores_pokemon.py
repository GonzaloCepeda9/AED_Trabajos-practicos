# 15. Entrenadores Pókemon
'''
Se cuenta con una lista de entrenadores Pokémon. De cada uno de estos se conoce: nombre, cantidad de torneos ganados, cantidad de batallas perdidas y cantidad de batallas ganadas. Y además la lista de sus Pokémons, de los cuales se sabe: nombre, nivel, tipo y subtipo. Se pide resolver las siguientes actividades utilizando lista de lista implementando las funciones necesarias:
a. obtener la cantidad de Pokémons de un determinado entrenador;
b. listar los entrenadores que hayan ganado más de tres torneos;
c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
d. mostrar todos los datos de un entrenador y sus Pokémos;
e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79%;
f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador (tipo y subtipo);
g. el promedio de nivel de los Pokémons de un determinado entrenador;
h. determinar cuántos entrenadores tienen a un determinado Pokémon;
i. mostrar los entrenadores que tienen Pokémons repetidos;
j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull;
k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se deberán mostrar los datos de ambos;
'''

from TDA_list import List
from ej15_class_entrenador_pokemon import Entrenador_Pokemon
from ej15_class_pokemon import Pokemon

# --------- CREACIÓN DE LISTA --------- #
lista_entrenadores = List()

# --------- CREACIÓN DE FUNCIONES PARA ORDENAR POR CRITERIO --------- #
def order_by_name(entrenador):
    return entrenador.nombre

# --------- AGREGACIÓN DE CRITERIOS DE BÚSQUEDA --------- #
lista_entrenadores.add_criterion('nombre', order_by_name)

# --------- CARGA DE DATOS EN LA LISTA --------- #

# Entrenadores
lista_entrenadores.insert_value(Entrenador_Pokemon('Ash Ketchum', 8, 15, 85))
lista_entrenadores.insert_value(Entrenador_Pokemon('Misty', 4, 8, 42))
lista_entrenadores.insert_value(Entrenador_Pokemon('Brock', 6, 35, 25))
lista_entrenadores.insert_value(Entrenador_Pokemon('Gary Oak', 5, 10, 70))
lista_entrenadores.insert_value(Entrenador_Pokemon('Cynthia', 12, 5, 95))
lista_entrenadores.insert_value(Entrenador_Pokemon('Leon', 10, 7, 83))
lista_entrenadores.insert_value(Entrenador_Pokemon('Iris', 3, 30, 20))
lista_entrenadores.insert_value(Entrenador_Pokemon('Steven Stone', 7, 6, 64))
lista_entrenadores.insert_value(Entrenador_Pokemon('Diantha', 4, 4, 52))
lista_entrenadores.insert_value(Entrenador_Pokemon('Red', 9, 20, 80))

# Pókemons de Ash
entrenador = 'Ash Ketchum'
position = lista_entrenadores.search('nombre', entrenador)
if position is not None:
    lista_entrenadores[position].lista_pokemons.insert_value(Pokemon('Pikachu', 80, 'Eléctrico', None))
    lista_entrenadores[position].lista_pokemons.insert_value(Pokemon('Wingull', 32, 'Agua', 'Volador'))
    lista_entrenadores[position].lista_pokemons.insert_value(Pokemon('Charizard', 78, 'Fuego', 'Volador'))
    lista_entrenadores[position].lista_pokemons.insert_value(Pokemon('Sceptile', 75, 'Planta', None))
    lista_entrenadores[position].lista_pokemons.insert_value(Pokemon('Wingull', 32, 'Agua', 'Volador'))
else:
    print(f'El entrenador {entrenador} no se encuentra en la lista de entrenadores.')

# Pókemons de Misty
entrenador = 'Misty'
position = lista_entrenadores.search('nombre', entrenador)
if position is not None:
    lista_entrenadores[position].lista_pokemons.insert_value(Pokemon('Starmie', 65, 'Agua', 'Psíquico'))
    lista_entrenadores[position].lista_pokemons.insert_value(Pokemon('Gyarados', 72, 'Agua', 'Volador'))
    lista_entrenadores[position].lista_pokemons.insert_value(Pokemon('Psyduck', 40, 'Agua', None))
    lista_entrenadores[position].lista_pokemons.insert_value(Pokemon('Wingull', 35, 'Agua', 'Volador'))
else:
    print(f'El entrenador {entrenador} no se encuentra en la lista de entrenadores.')

# Pókemons de Brock
entrenador = 'Brock'
position = lista_entrenadores.search('nombre', entrenador)
if position is not None:
    lista_entrenadores[position].lista_pokemons.insert_value(Pokemon('Onix', 55, 'Roca', 'Tierra'))
    lista_entrenadores[position].lista_pokemons.insert_value(Pokemon('Geodude', 48, 'Roca', 'Tierra'))
    lista_entrenadores[position].lista_pokemons.insert_value(Pokemon('Tyrantrum', 72, 'Roca', 'Dragón'))
    lista_entrenadores[position].lista_pokemons.insert_value(Pokemon('Steelix', 68, 'Acero', 'Tierra'))
    lista_entrenadores[position].lista_pokemons.insert_value(Pokemon('Onix', 55, 'Roca', 'Tierra'))
else:
    print(f'El entrenador {entrenador} no se encuentra en la lista de entrenadores.')

# Pókemons de Gary Oak
entrenador = 'Gary Oak'
position = lista_entrenadores.search('nombre', entrenador)
if position is not None:
    lista_entrenadores[position].lista_pokemons.insert_value(Pokemon('Blastoise', 82, 'Agua', None))
    lista_entrenadores[position].lista_pokemons.insert_value(Pokemon('Arcanine', 75, 'Fuego', None))
    lista_entrenadores[position].lista_pokemons.insert_value(Pokemon('Umbreon', 70, 'Siniestro', None))
    lista_entrenadores[position].lista_pokemons.insert_value(Pokemon('Tyrantrum', 68, 'Roca', 'Dragón'))
else:
    print(f'El entrenador {entrenador} no se encuentra en la lista de entrenadores.')

# Pókemons de Cynthia
entrenador = 'Cynthia'
position = lista_entrenadores.search('nombre', entrenador)
if position is not None:
    lista_entrenadores[position].lista_pokemons.insert_value(Pokemon('Garchomp', 95, 'Dragón', 'Tierra'))
    lista_entrenadores[position].lista_pokemons.insert_value(Pokemon('Lucario', 82, 'Lucha', 'Acero'))
    lista_entrenadores[position].lista_pokemons.insert_value(Pokemon('Roserade', 78, 'Planta', 'Veneno'))
    lista_entrenadores[position].lista_pokemons.insert_value(Pokemon('Spiritomb', 76, 'Fantasma', 'Siniestro'))
    lista_entrenadores[position].lista_pokemons.insert_value(Pokemon('Scovillain', 85, 'Planta', 'Fuego'))
else:
    print(f'El entrenador {entrenador} no se encuentra en la lista de entrenadores.')

# Pókemons de Leon
entrenador = 'Leon'
position = lista_entrenadores.search('nombre', entrenador)
if position is not None:
    lista_entrenadores[position].lista_pokemons.insert_value(Pokemon('Charizard', 96, 'Fuego', 'Volador'))
    lista_entrenadores[position].lista_pokemons.insert_value(Pokemon('Aegislash', 84, 'Acero', 'Fantasma'))
    lista_entrenadores[position].lista_pokemons.insert_value(Pokemon('Dragapult', 88, 'Dragón', 'Fantasma'))
    lista_entrenadores[position].lista_pokemons.insert_value(Pokemon('Rillaboom', 80, 'Planta', None))
else:
    print(f'El entrenador {entrenador} no se encuentra en la lista de entrenadores.')

# Pókemons de Iris
entrenador = 'Iris'
position = lista_entrenadores.search('nombre', entrenador)
if position is not None:
    lista_entrenadores[position].lista_pokemons.insert_value(Pokemon('Haxorus', 76, 'Dragón', None))
    lista_entrenadores[position].lista_pokemons.insert_value(Pokemon('Dragonite', 81, 'Dragón', 'Volador'))
    lista_entrenadores[position].lista_pokemons.insert_value(Pokemon('Excadrill', 70, 'Tierra', 'Acero'))
    lista_entrenadores[position].lista_pokemons.insert_value(Pokemon('Wingull', 28, 'Agua', 'Volador'))
else:
    print(f'El entrenador {entrenador} no se encuentra en la lista de entrenadores.')

# Pókemons de Steven Stone
entrenador = 'Steven Stone'
position = lista_entrenadores.search('nombre', entrenador)
if position is not None:
    lista_entrenadores[position].lista_pokemons.insert_value(Pokemon('Metagross', 92, 'Acero', 'Psíquico'))
    lista_entrenadores[position].lista_pokemons.insert_value(Pokemon('Aggron', 78, 'Acero', 'Roca'))
    lista_entrenadores[position].lista_pokemons.insert_value(Pokemon('Terrakion', 80, 'Roca', 'Lucha'))
    lista_entrenadores[position].lista_pokemons.insert_value(Pokemon('Skarmory', 73, 'Acero', 'Volador'))
else:
    print(f'El entrenador {entrenador} no se encuentra en la lista de entrenadores.')

# Pókemons de Diantha
entrenador = 'Diantha'
position = lista_entrenadores.search('nombre', entrenador)
if position is not None:
    lista_entrenadores[position].lista_pokemons.insert_value(Pokemon('Gardevoir', 88, 'Psíquico', 'Hada'))
    lista_entrenadores[position].lista_pokemons.insert_value(Pokemon('Goodra', 79, 'Dragón', None))
    lista_entrenadores[position].lista_pokemons.insert_value(Pokemon('Tyrantrum', 65, 'Roca', 'Dragón'))
    lista_entrenadores[position].lista_pokemons.insert_value(Pokemon('Aurorus', 67, 'Roca', 'Hielo'))
else:
    print(f'El entrenador {entrenador} no se encuentra en la lista de entrenadores.')

# Pókemons de Red
entrenador = 'Red'
position = lista_entrenadores.search('nombre', entrenador)
if position is not None:
    lista_entrenadores[position].lista_pokemons.insert_value(Pokemon('Pikachu', 90, 'Eléctrico', None))
    lista_entrenadores[position].lista_pokemons.insert_value(Pokemon('Venusaur', 85, 'Planta', 'Veneno'))
    lista_entrenadores[position].lista_pokemons.insert_value(Pokemon('Blastoise', 84, 'Agua', None))
    lista_entrenadores[position].lista_pokemons.insert_value(Pokemon('Charizard', 86, 'Fuego', 'Volador'))
    lista_entrenadores[position].lista_pokemons.insert_value(Pokemon('Scovillain', 70, 'Planta', 'Fuego'))
else:
    print(f'El entrenador {entrenador} no se encuentra en la lista de entrenadores.')

# --------- CREACIÓN DE FUNCIONES PARA FORMATO --------- #
class Color:
    RESET   = '\033[0m'
    NEGRITA = '\033[1m'
    CIAN    = '\033[96m'
    ROJO    = '\033[38;2;171;29;29m'     #AB1D1D
    AMARILLO= '\033[38;2;227;187;45m'    #E3BB2D
    AZUL    = '\033[38;2;0;48;176m'      #0030B0
    VERDE   = '\033[38;2;12;120;0m'      #0C7800
    VIOLETA = '\033[38;2;88;31;122m'     #581F7A

def print_seccion(titulo, ancho=140, relleno="-", color=Color.VERDE):
    print(f'\n{color}{f" {titulo} ".center(ancho, relleno)}{Color.RESET}')

#################################################  EJECUCIÓN DE PRUEBAS DEL ENUNCIADO  #################################################
print(f'\n{Color.CIAN}{f' EJERCICIO 15: ENTRENADORES PÓKEMON '.center(140, "=")}{Color.RESET}')
print_seccion('Información completa de entrenadores y sus pókemons')
print(f'{Color.AZUL}Lista original:{Color.RESET}')
for entrenador in lista_entrenadores:
    print(f'\n  → {entrenador}')
    if not entrenador.lista_pokemons.is_empty():
        print(f'\n    Pókemons de {entrenador.nombre}:')
        for pokemon in entrenador.lista_pokemons:
            print(f'    - {pokemon}')
    else:
        print(f'\n    {entrenador.nombre} no tiene Pókemons.')

# a. obtener la cantidad de Pokémons de un determinado entrenador;
print_seccion('a. obtener la cantidad de Pokémons de un determinado entrenador;')
entrenador = 'Ash Ketchum'
position = lista_entrenadores.search('nombre', entrenador)
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
if position is not None:
    cantidad = lista_entrenadores[position].lista_pokemons.size()
    if cantidad > 0:
        print(f'  → El entrenador {entrenador} tiene {cantidad} Pókemons.')
    else:      
        print(f'  → El entrenador {entrenador} no tiene ningún Pókemon.')
else:
    print(f'  → El entrenador no se encuentra en la lista.')

# b. listar los entrenadores que hayan ganado más de tres torneos;
print_seccion('b. listar los entrenadores que hayan ganado más de tres torneos;')
lista_entrenadores_victoriosos = List()
cantidad = 3
for entrenador in lista_entrenadores:
    if entrenador.torneos_ganados > cantidad:
        lista_entrenadores_victoriosos.insert_value(entrenador)
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
if not lista_entrenadores_victoriosos.is_empty():
    for entrenador in lista_entrenadores_victoriosos:
        print(f'  → {entrenador.nombre}')
else:
    print(f'  → No se encontraron entrenadores con más de {cantidad} torneos ganados.')

# c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
print_seccion('c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;')
cantidad_mayor_torneos = 0
entrenador_mas_ganador = None
for entrenador in lista_entrenadores:
    if entrenador.torneos_ganados > cantidad_mayor_torneos:
        cantidad_mayor_torneos = entrenador.torneos_ganados
        entrenador_mas_ganador = entrenador

mayor_nivel = 0
lista_pokemons_mayor_nivel = List()
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
if entrenador_mas_ganador is not None:
    if not entrenador_mas_ganador.lista_pokemons.is_empty():
        for pokemon in entrenador_mas_ganador.lista_pokemons:
            if pokemon.nivel > mayor_nivel:
                mayor_nivel = pokemon.nivel

        for pokemon in entrenador_mas_ganador.lista_pokemons:
            if pokemon.nivel == mayor_nivel:
                lista_pokemons_mayor_nivel.insert_value(pokemon)

        if not lista_pokemons_mayor_nivel.is_empty():
            print(f'  → Entrenador: {entrenador_mas_ganador.nombre} | Torneos ganados: {entrenador_mas_ganador.torneos_ganados}')
            for pokemon in lista_pokemons_mayor_nivel:
                print(f'  → Pókemon: {pokemon.nombre} | Nivel: {pokemon.nivel}')
    else:
        print(f'  → El entrenador {entrenador_mas_ganador.nombre} no tiene ningún Pókemon.')
else:
    print(f'  → No se encontró ningún entrenador con torneos ganados.')

# d. mostrar todos los datos de un entrenador y sus Pokémos;
print_seccion('d. mostrar todos los datos de un entrenador y sus Pokémos;')
entrenador = 'Misty'
position = lista_entrenadores.search('nombre', entrenador)
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
if position is not None:
    print(f'  → {lista_entrenadores[position]}')
    if not lista_entrenadores[position].lista_pokemons.is_empty():
        print(f'\n    Pókemons de {entrenador}')
        for pokemon in lista_entrenadores[position].lista_pokemons:
            print(f'    - {pokemon}')
    else:
        print(f'  → El entrenador no tiene ningún Pókemon')
else:
    print(f'  → El entrenador {entrenador} no se encuentra en la lista.')

# e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79%;
print_seccion('e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79%;')
porcentaje_buscado = 79
entrenadores_mas_ganadores = List()

for entrenador in lista_entrenadores:
    total_batallas = entrenador.batallas_ganadas + entrenador.batallas_perdidas
    if total_batallas > 0:
        porcentaje_batallas_ganadas = entrenador.batallas_ganadas * 100 / total_batallas
        if porcentaje_batallas_ganadas > porcentaje_buscado:
            entrenadores_mas_ganadores.insert_value(entrenador)

print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
if not entrenadores_mas_ganadores.is_empty():
    for entrenador in entrenadores_mas_ganadores:
        total_batallas = entrenador.batallas_ganadas + entrenador.batallas_perdidas
        porcentaje_batallas_ganadas = entrenador.batallas_ganadas * 100 / total_batallas
        print(f'  → {entrenador.nombre} | Porcentaje: {round(porcentaje_batallas_ganadas, 1)}%')
else:
    print(f'  → No se encontraron entrenadores cuyo porcentaje de batallas ganadas sea mayor a {porcentaje_buscado}%.')
        
# f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador (tipo y subtipo);
print_seccion('f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador (tipo y subtipo);')
lista_entrenadores_buscados = List()
tipo_1 = 'Planta'
subtipo_1 = 'Fuego'
tipo_2 = 'Agua'
subtipo_2 = 'Volador'
for entrenador in lista_entrenadores:
    for pokemon in entrenador.lista_pokemons:
        if (pokemon.tipo == tipo_1 and pokemon.subtipo == subtipo_1) or (pokemon.tipo == tipo_2 and pokemon.subtipo == subtipo_2):
            lista_entrenadores_buscados.insert_value(entrenador)
            break

print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
if not lista_entrenadores_buscados.is_empty():
    for entrenador in lista_entrenadores_buscados:
        print(f'\n  → Entrenador: {entrenador.nombre}')

        lista_nombres_pokemons = List()
        lista_pokemons_no_repetidos = List()
        for pokemon in entrenador.lista_pokemons:
            if pokemon.nombre not in lista_nombres_pokemons:
                lista_nombres_pokemons.insert_value(pokemon.nombre)
                lista_pokemons_no_repetidos.insert_value(pokemon)

        for pokemon in lista_pokemons_no_repetidos:
            if (pokemon.tipo == tipo_1 and pokemon.subtipo == subtipo_1) or (pokemon.tipo == tipo_2 and pokemon.subtipo == subtipo_2):
                print(f'    - {pokemon.nombre} | Tipo: {pokemon.tipo} | Subtipo: {pokemon.subtipo}')
else:
    print(f'  → No se encontraron entrenadores que tengan Pókemons de tipo {tipo_1}/{subtipo_1} ó {tipo_2}/{subtipo_2}.')

print(f'\n# Aclaración: Se invirtió el tipo/subtipo fuego/planta por planta/fuego, simplemente para probar otra combinación existente. ')

# g. el promedio de nivel de los Pokémons de un determinado entrenador;
print_seccion('g. el promedio de nivel de los Pokémons de un determinado entrenador;')
entrenador_buscado = 'Ash Ketchum'
position = lista_entrenadores.search('nombre', entrenador_buscado)

print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
if position is not None:
    suma_niveles = 0
    for pokemon in lista_entrenadores[position].lista_pokemons:
        suma_niveles += pokemon.nivel
    cantidad_pokemons = lista_entrenadores[position].lista_pokemons.size()
    if cantidad_pokemons > 0:
        promedio_niveles = suma_niveles / cantidad_pokemons
        print(f'  → El promedio de niveles de los Pókemons de {entrenador_buscado} es de {round(promedio_niveles, 1)}.')
    else:
        print(f'  → El entrenador no tiene ningún Pókemon.')
else:
    print(f'  → El entrenador no se encuentra en la lista.')

# h. determinar cuántos entrenadores tienen a un determinado Pokémon;
print_seccion('h. determinar cuántos entrenadores tienen a un determinado Pokémon;')
lista_entrenadores_pokemon = List()
pokemon_determinado = 'Charizard'
for entrenador in lista_entrenadores:
    for pokemon in entrenador.lista_pokemons:
        if pokemon.nombre == pokemon_determinado:
            lista_entrenadores_pokemon.insert_value(entrenador.nombre)
            break

print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
if not lista_entrenadores_pokemon.is_empty():
    print(f'  → Cantidad de entrenadores que poseen a {pokemon_determinado}: {lista_entrenadores_pokemon.size()}.')
else:
    print(f'  → No se encontraron entrenadores que posean al Pókemon "{pokemon_determinado}".')

# i. mostrar los entrenadores que tienen Pokémons repetidos;
print_seccion('i. mostrar los entrenadores que tienen Pokémons repetidos;')
lista_entrenadores_pokemon_repetidos = List()

for entrenador in lista_entrenadores:
    lista_pokemon_aux = List()
    pokemon_repetido = False
    for pokemon in entrenador.lista_pokemons:
        if lista_pokemon_aux.is_empty():
            lista_pokemon_aux.insert_value(pokemon.nombre)
        else:
            if pokemon.nombre in lista_pokemon_aux:
                pokemon_repetido = True
                lista_entrenadores_pokemon_repetidos.insert_value(entrenador)
                break
            else:
                lista_pokemon_aux.insert_value(pokemon.nombre)

print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
if not lista_entrenadores_pokemon_repetidos.is_empty():
    for entrenador in lista_entrenadores_pokemon_repetidos:
        print(f'  → {entrenador.nombre}')
else:
    print(f'  → Ningún entrenador de la lista tiene Pókemons repetidos.')
        
# j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull;
print_seccion('j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull;')
lista_entrenadores_aux = List()
pokemon_1 = 'Tyrantrum'
pokemon_2 = 'Terrakion'
pokemon_3 = 'Wingull'
pokemons_especificos = (pokemon_1, pokemon_2, pokemon_3)

for entrenador in lista_entrenadores:
    for pokemon in entrenador.lista_pokemons:
        if pokemon.nombre in pokemons_especificos:
            lista_entrenadores_aux.insert_value(entrenador)
            break

print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
if not lista_entrenadores_aux.is_empty():
    for entrenador in lista_entrenadores_aux:
        print(f'  → {entrenador.nombre}')
else:
    print(f'  → No se encontraron entrenadores que tengan a los Pókemons {pokemon_1}, {pokemon_2} o {pokemon_3}.')

# k. determinar si un entrenador "X" tiene al Pokémon "Y", tanto el nombre del entrenador como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se deberán mostrar los datos de ambos;
print_seccion('k. determinar si un entrenador "X" tiene al Pokémon "Y"...')

print(f'{Color.AZUL}Datos ingresados:{Color.RESET}')
entrenador_buscado = input(f'  → Nombre del entrenador: ')
pokemon_buscado = input(f'  → Nombre del Pókemon: ')

print(f'\n{Color.VIOLETA}Resultado:{Color.RESET}')
if entrenador_buscado == "":
    print(f'  → Debe ingresar el nombre del entrenador.')
else:
    if pokemon_buscado == "":
        print(f'  → Debe ingresar el nombre del Pókemon.')
    else:
        position_entrenador = lista_entrenadores.search('nombre', entrenador_buscado)

        if position_entrenador is not None:
            position_pokemon = lista_entrenadores[position_entrenador].lista_pokemons.search('nombre', pokemon_buscado)
            if position_pokemon is not None:
                print(f'  → El entrenador {entrenador_buscado} tiene al Pókemon {pokemon_buscado}.')
                print(f'\n  → Entrenador:')
                print(f'    - {lista_entrenadores[position_entrenador]}')
                print(f'\n  → Pókemon:')
                print(f'    - {lista_entrenadores[position_entrenador].lista_pokemons[position_pokemon]}')
            else:
                print(f'  → El entrenador {entrenador_buscado} no tiene al Pókemon {pokemon_buscado}.')
        else:
            print(f'  → El entrenador {entrenador_buscado} no se encuentra en la lista.')

print(f'\n{Color.CIAN}{f" FIN DE EJECUCIÓN DEL PROGRAMA ".center(140, "=")}{Color.RESET}')
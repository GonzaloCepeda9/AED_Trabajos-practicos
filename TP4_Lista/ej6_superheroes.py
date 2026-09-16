# Superhéroes de comics
'''
6. Dada una lista de superhéroes de comics, de los cuales se conoce su nombre, año aparición, casa de comic a la que pertenece (Marvel o DC) y biografía, implementar la funciones necesarias para poder realizar las siguientes actividades:
a. eliminar el nodo que contiene la información de Linterna Verde;
b. mostrar el año de aparición de Wolverine;
c. cambiar la casa de Dr. Strange a Marvel;
d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra “traje” o “armadura”;
e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición sea anterior a 1963;
f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
g. mostrar toda la información de Flash y Star-Lord;
h. listar los superhéroes que comienzan con la letra B, M y S;
i. determinar cuántos superhéroes hay de cada casa de comic.
'''

from TDA_list import List
from ej6_class_superheroe import Superheroe

# --------- CREACIÓN DE LISTA --------- #
lista_superheroes = List()

# --------- CREACIÓN DE FUNCIONES PARA ORDENAR POR CRITERIO --------- #

def order_by_name(element):
    return element.nombre

def order_by_year(element):
    return element.anio_aparicion

def order_by_house(element):
    return element.casa_comic

def order_by_biography(element):
    return element.biografia

# --------- AGREGACIÓN DE CRITERIOS DE BÚSQUEDA --------- #
lista_superheroes.add_criterion('nombre', order_by_name)
lista_superheroes.add_criterion('anio_aparicion', order_by_year)
lista_superheroes.add_criterion('casa_comic', order_by_house)
lista_superheroes.add_criterion('biografia', order_by_biography)

# --------- CARGA DE DATOS EN LA LISTA --------- #
lista_superheroes.insert_value(Superheroe("Spider-Man", 1962, "Marvel", "Joven que obtiene poderes tras ser picado por una araña radiactiva."))
lista_superheroes.insert_value(Superheroe("Wolverine", 1974, "Marvel", "Mutante con garras de adamantium y factor de curación."))
lista_superheroes.insert_value(Superheroe("Dr. Strange", 1963, "DC", "Hechicero supremo que protege la Tierra de amenazas místicas."))  # Inicialmente DC para probar cambio
lista_superheroes.insert_value(Superheroe("Iron Man", 1963, "Marvel", "Genio multimillonario que construye un traje de alta tecnología."))
lista_superheroes.insert_value(Superheroe("Capitana Marvel", 1968, "Marvel", "Piloto que obtiene poderes cósmicos."))
lista_superheroes.insert_value(Superheroe("Mujer Maravilla", 1941, "DC", "Princesa amazona con fuerza sobrehumana."))
lista_superheroes.insert_value(Superheroe("Flash", 1940, "DC", "Posee velocidad sobrehumana gracias a la Fuerza de la Velocidad."))
lista_superheroes.insert_value(Superheroe("Star-Lord", 1976, "Marvel", "Líder de los Guardianes de la Galaxia, usa un traje espacial."))
lista_superheroes.insert_value(Superheroe("Batman", 1939, "DC", "Vigilante que usa una armadura y artilugios."))
lista_superheroes.insert_value(Superheroe("Superman", 1938, "DC", "Kryptoniano con poderes solares."))
lista_superheroes.insert_value(Superheroe("Linterna Verde", 1940, "DC", "Miembro del cuerpo de linternas verdes, usa un anillo de poder."))

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
print(f'\n{Color.CIAN}{f' EJERCICIO 6: SUPERHÉROES DE COMICS '.center(140, "=")}{Color.RESET}')
print_seccion('Información completa de superhéroes')
print(f'{Color.AZUL}Lista original:{Color.RESET}')
for superheroe in lista_superheroes:
    print(f'  → {superheroe}')

# a. eliminar el nodo que contiene la información de Linterna Verde;
print_seccion('a. eliminar el nodo que contiene la información de Linterna Verde;')
nombre_elemento = 'Linterna Verde'
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
eliminado = lista_superheroes.delete_value('nombre', nombre_elemento)
if eliminado is not None:
    print(f'  → Nodo eliminado: {eliminado.nombre}.')
    print(f'{Color.AZUL}\nLista actualizada:{Color.RESET}')
    for superheroe in lista_superheroes:
        print(f'  → {superheroe.nombre}')
else:
    print(f'  → El superhéroe "{nombre_elemento}" no se encuentra en la lista.')

# b. mostrar el año de aparición de Wolverine;
print_seccion('b. mostrar el año de aparición de Wolverine;')
nombre_superheroe = 'Wolverine'
position = lista_superheroes.search('nombre', nombre_superheroe)
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
if position is not None:
    print(f'  → Año de aparición de {nombre_superheroe}: {lista_superheroes[position].anio_aparicion}.')
else:
    print(f'  → El superhéroe "{nombre_superheroe}" no se encuentra en la lista.')

# c. cambiar la casa de Dr. Strange a Marvel;
print_seccion('c. cambiar la casa de Dr. Strange a Marvel;')
nombre_superheroe = 'Dr. Strange'
casa_nueva = 'Marvel'
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
position = lista_superheroes.search('nombre', nombre_superheroe)
if position is not None:
    lista_superheroes[position].casa_comic = casa_nueva
    print(f'  → La casa del superhéroe {nombre_superheroe} ha sido actualizada correctamente.')
    print(f'{Color.AZUL}\nLista actualizada:{Color.RESET}')
    for superheroe in lista_superheroes:
        print(f'  → {superheroe.nombre} | Casa: {superheroe.casa_comic}')
else:
    print(f'  → El superhéroe "{nombre_superheroe}" no se encuentra en la lista.')

# d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra “traje” o “armadura”;
print_seccion('d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra "traje" o "armadura";')
palabra1 = 'traje'
palabra2 = 'armadura'
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
lista_superheroes_aux = List()
for superheroe in lista_superheroes:
    if palabra1 in superheroe.biografia or palabra2 in superheroe.biografia:
        lista_superheroes_aux.insert_value(superheroe)
if not lista_superheroes_aux.is_empty():
    for superheroe in lista_superheroes_aux:
        print(f'  → {superheroe.nombre}')
else:
    print(f'  → No se encontraron superhéroes cuya biografía incluya la palabra "{palabra1}" o "{palabra2}".')

# e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición sea anterior a 1963;
print_seccion('e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición sea anterior a 1963;')
anio = 1963
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
lista_superheroes_aux = List()
for superheroe in lista_superheroes:
    if superheroe.anio_aparicion < anio:
        lista_superheroes_aux.insert_value(superheroe)
if not lista_superheroes_aux.is_empty():
    for superheroe in lista_superheroes_aux:
        print(f'  → Nombre: {superheroe.nombre} | Casa: {superheroe.casa_comic}')
else:
    print(f'  → No se encontraron superhéroes cuya fecha de aparición sea anterior al año {anio}.')

# f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
print_seccion('f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;')
superheroe1 = 'Capitana Marvel'
superheroe2 = 'Mujer Maravilla'
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
position1 = lista_superheroes.search('nombre', superheroe1)
if position1 is not None:
    print(f'  → {superheroe1} | Casa a la que pertenece: {lista_superheroes[position1].casa_comic}.')
else:
    print(f'  → El superhéroe {superheroe1} no se encuentra en la lista.')

position2 = lista_superheroes.search('nombre', superheroe2)
if position2 is not None:
    print(f'  → {superheroe2} | Casa a la que pertenece: {lista_superheroes[position2].casa_comic}.')
else:
    print(f'  → El superhéroe {superheroe2} no se encuentra en la lista.')

# g. mostrar toda la información de Flash y Star-Lord;
print_seccion('g. mostrar toda la información de Flash y Star-Lord;')
superheroe1 = 'Flash'
superheroe2 = 'Star-Lord'
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')

position = lista_superheroes.search('nombre', superheroe1)
if position is not None:
    print(f'  → {lista_superheroes[position]}')
else:
    print(f'  → El superhéroe {superheroe1} no se encuentra en la lista.')

position = lista_superheroes.search('nombre', superheroe2)
if position is not None:
    print(f'  → {lista_superheroes[position]}')
else:
    print(f'  → El superhéroe {superheroe2} no se encuentra en la lista.')

# h. listar los superhéroes que comienzan con la letra B, M y S;
print_seccion('h. listar los superhéroes que comienzan con la letra B, M y S;')
inicial1 = 'B'
inicial2 = 'M'
inicial3 = 'S'
iniciales = (inicial1, inicial2, inicial3)
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
lista_superheroes_aux = List()
for superheroe in lista_superheroes:
    if superheroe.nombre.startswith(iniciales):
        lista_superheroes_aux.insert_value(superheroe)
if not lista_superheroes_aux.is_empty():
    for superheroe in lista_superheroes_aux:
        print(f'  → {superheroe.nombre}')
else:
    print(f'  → No se encontraron superhéroes cuyos nombres comienzan con las iniciales {inicial1}, {inicial2} o {inicial3}.')

# i. determinar cuántos superhéroes hay de cada casa de comic.
print_seccion('i. determinar cuántos superhéroes hay de cada casa de comic.')
casa_comic1 = 'Marvel'
casa_comic2 = 'DC'
cantidad_casa1 = 0
cantidad_casa2 = 0
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
for superheroe in lista_superheroes:
    if superheroe.casa_comic == casa_comic1:
        cantidad_casa1 += 1
    elif superheroe.casa_comic == casa_comic2:
        cantidad_casa2 += 1

if cantidad_casa1 > 0:
    print(f'  → En la casa de comic {casa_comic1} hay {cantidad_casa1} superhéroes.')
else:
    print(f'  → No se encontraron superhéroes de la casa de comic {casa_comic1}')

if cantidad_casa2 > 0:
    print(f'  → En la casa de comic {casa_comic2} hay {cantidad_casa2} superhéroes.')
else:
    print(f'  → No se encontraron superhéroes de la casa de comic {casa_comic2}')

print(f'\n{Color.CIAN}{f' FIN DE EJECUCIÓN DEL PROGRAMA '.center(140, "=")}{Color.RESET}')
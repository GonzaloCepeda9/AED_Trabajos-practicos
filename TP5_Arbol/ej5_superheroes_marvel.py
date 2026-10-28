# 5. Superhéroes y villanos de Marvel Cinematic Universe (MCU)
'''
Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Universe (MCU), desarrollar un algoritmo que contemple lo siguiente:
a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo booleano que indica si es un héroe o un villano, True y False respectivamente;
b. listar los villanos ordenados alfabéticamente;
c. mostrar todos los superhéroes que empiezan con C;
d. determinar cuántos superhéroes hay el árbol;
e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para encontrarlo en el árbol y modificar su nombre;
f. listar los superhéroes ordenados de manera descendente;
g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a los villanos, luego resolver las siguiente tareas:
    I. determinar cuántos nodos tiene cada árbol;
    II. realizar un barrido ordenado alfabéticamente de cada árbol.
'''

from TDA_list import List
from TDA_tree import BinaryTree
from ej5_lista_personajes_comic import lista_personajes_comic
from typing import Any, Optional

# --------- CREACIÓN DE FUNCIONES ADICIONALES --------- #

class BinaryTreePersonajes(BinaryTree):

    # b. listar los villanos ordenados alfabéticamente;
    
    def listar_villanos(self):
        def __listar_villanos(root):
            if root is not None:
                __listar_villanos(root.left)
                if root.other_values['is_villain'] == True:
                        print(f'  → {root.value}')
                __listar_villanos(root.right)

        if self.root is not None:
            __listar_villanos(self.root)

    # c. mostrar todos los superhéroes que empiezan con C;

    def mostrar_por_inicial(self):
        def __mostrar_por_inicial(root):
            if root is not None:
                __mostrar_por_inicial(root.left)
                if root.other_values['is_villain'] is False and root.value.startswith('C'):
                    print(f'  → {root.value}')
                __mostrar_por_inicial(root.right)

        if self.root is not None:
            __mostrar_por_inicial(self.root)

    # d. determinar cuántos superhéroes hay el árbol;

    def determinar_superheroes(self):
        def __determinar_superheroes(root, contador: int = 0):
            if root is not None:
                contador = __determinar_superheroes(root.left, contador)
                if root.other_values['is_villain'] == False:
                    contador += 1
                contador = __determinar_superheroes(root.right, contador)
            return contador

        if self.root is None:
            return 0

        return __determinar_superheroes(self.root)

    # e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para encontrarlo en el árbol y modificar su nombre;

    def proximity_search(self, value: Any) -> List:
        def __search(root, value, resultados):
            if root is not None:
                if root.value.startswith(value):
                    resultados.insert_value(root)
                __search(root.left, value, resultados)
                __search(root.right, value, resultados)

        resultados = List()
        if self.root is not None:
            __search(self.root, value, resultados)

        return resultados

    # f. listar los superhéroes ordenados de manera descendente;
    
    def listar_superheroes_descendente(self):
        def __listar_superheroes_descendente(root):
            if root is not None:
                __listar_superheroes_descendente(root.right)
                if root.other_values['is_villain'] == False:
                        print(f'  → {root.value}')
                __listar_superheroes_descendente(root.left)

        if self.root is not None:
            __listar_superheroes_descendente(self.root)

    # g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a los villanos, luego resolver las siguiente tareas:

    def insertar_por_campo(self, value: Any, other_values: Optional[Any] = None):
        def __insertar_por_campo(root, value, other_values):
            if root is None:
                nodo = BinaryTree.__nodeTree(value, other_values)
                return nodo
            elif other_values['is_villain'] == False:
                root.left = __insertar_por_campo(root.left, value, other_values)
            else:
                root.right = __insertar_por_campo(root.right, value, other_values)
            return root

        self.root = __insertar_por_campo(self.root, value, other_values)

    #     I. determinar cuántos nodos tiene cada árbol;

    def determinar_superheroe_o_supervillano(self: BinaryTree):
        def __determinar_superheroe_o_supervillano(root, contador_superheroes: int = 0, contador_supervillanos: int = 0):
            if root is not None:
                contador_superheroes, contador_supervillanos = __determinar_superheroe_o_supervillano(root.left, contador_superheroes, contador_supervillanos)
                if root.other_values['is_villain'] == False:
                    contador_superheroes += 1
                else:
                    contador_supervillanos += 1
                contador_superheroes, contador_supervillanos = __determinar_superheroe_o_supervillano(root.right, contador_superheroes, contador_supervillanos)
            return contador_superheroes, contador_supervillanos

        if self.root is None:
            return 0, 0

        return __determinar_superheroe_o_supervillano(self.root)

    #     II. realizar un barrido ordenado alfabéticamente de cada árbol.

# --------- CARGA DE DATOS --------- #

arbol_personajes = BinaryTreePersonajes()

for personaje in lista_personajes_comic:
    arbol_personajes.insert(personaje['nombre'], personaje)

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

def print_seccion_extra(titulo, ancho=140, relleno=" ", color=Color.VERDE):
    print(f'{color}{f" {titulo} ".center(ancho, relleno)}{Color.RESET}')

#################################################  EJECUCIÓN DE PRUEBAS DEL ENUNCIADO  #################################################
print(f'\n{Color.CIAN}{f' EJERCICIO 5: PERSONAJES DE MARVEL CINEMATIC UNIVERSE (MCU) '.center(140, "=")}{Color.RESET}')

print_seccion('Información completa de personajes')
print(f'{Color.AZUL}Lista original ordenada alfabéticamente:{Color.RESET}')
arbol_personajes.in_order()

# a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo booleano que indica si es un héroe o un villano, True y False respectivamente;
print_seccion('a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo booleano')
print_seccion_extra('que indica si es un héroe o un villano, True y False respectivamente;')
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
print(f'  → En el campo "other_values" de cada nodo del árbol se almacenó el campo booleano "is_villain".')

# b. listar los villanos ordenados alfabéticamente;
print_seccion('# b. listar los villanos ordenados alfabéticamente;')
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
arbol_personajes.listar_villanos()

# c. mostrar todos los superhéroes que empiezan con C;
print_seccion('c. mostrar todos los superhéroes que empiezan con C;')
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
arbol_personajes.mostrar_por_inicial()

# d. determinar cuántos superhéroes hay el árbol;
print_seccion('d. determinar cuántos superhéroes hay en el árbol;')
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
cantidad = arbol_personajes.determinar_superheroes()
if cantidad > 0:
    print(f'  → En el árbol hay {cantidad} superhéroes.')
else:
    print(f'  → No se encontraron superhéroes en el árbol.')

# e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para encontrarlo en el árbol y modificar su nombre;
print_seccion('e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad')
print_seccion_extra('para encontrarlo en el árbol y modificar su nombre;')
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')

buscado = 'Dr. Strange'
coincidencia_buscada = 'D'
coincidencias = arbol_personajes.proximity_search(coincidencia_buscada)

if not coincidencias.is_empty():

    print(f'  → Coincidencias encontradas para "{coincidencia_buscada}".')
    for coincidencia in coincidencias:
        print(f'    - {coincidencia.value}')

    modificado = False
    for nodo in coincidencias:
        if nodo.value == buscado:
            modificado = True
            aux_other_values = nodo.other_values
            arbol_personajes.delete('Dr. Strange')
            arbol_personajes.insert('Doctor Strange', aux_other_values)
            print(f'\n  → El nombre del personaje "{buscado}" ha sido modificado correctamente.')
            print(f'{Color.AZUL}\nLista actualizada:{Color.RESET}')
            arbol_personajes.in_order()
            break

    if modificado == False:
        print(f'\n  → El personaje {buscado} no se encontró entre las coincidencias.')
else:
    print(f'\n  → No se encontraron coincidencias para "{coincidencia_buscada}".')

# f. listar los superhéroes ordenados de manera descendente;
print_seccion('f. listar los superhéroes ordenados de manera descendente;')
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
arbol_personajes.listar_superheroes_descendente()

# g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a los villanos, luego resolver las siguiente tareas:
print_seccion('g. generar un bosque a partir de este árbol...')
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
print(f'  → Aún no desarrollado en clase.')

#     I. determinar cuántos nodos tiene cada árbol;
print_seccion_extra('\nI. determinar cuántos nodos tiene cada árbol;')
cantidad_superheroes, cantidad_supervillanos = arbol_personajes.determinar_superheroe_o_supervillano()
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
print(f'  → El subárbol de superhéroes contiene {cantidad_superheroes} nodos.')
print(f'  → El subárbol de supervillanos contiene {cantidad_supervillanos} nodos.')

#     II. realizar un barrido ordenado alfabéticamente de cada árbol.
print_seccion_extra('\nII. realizar un barrido ordenado alfabéticamente de cada árbol.')
arbol_v = BinaryTree()
arbol_f = BinaryTree()
condition = 'is_villain'
arbol_personajes.divide_tree(arbol_v, arbol_f, condition)
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
print(f'\n  Árbol de superhéroes ordenado alfabéticamente: ')
arbol_v.in_order()
print(f'\n  Árbol de supervillanos ordenado alfabéticamente: ')
arbol_f.in_order()

print(f'\n{Color.CIAN}{f" FIN DE EJECUCIÓN DEL PROGRAMA ".center(140, "=")}{Color.RESET}')
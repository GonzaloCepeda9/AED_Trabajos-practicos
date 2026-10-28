# 23. Criaturas y Dioses
'''
Implementar un algoritmo que permita generar un árbol con los datos de la siguiente tabla y resuelva las siguientes consultas:
a. listado inorden de las criaturas y quienes la derrotaron;
b. se debe permitir cargar una breve descripción sobre cada criatura;
c. mostrar toda la información de la criatura Talos;
d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
e. listar las criaturas derrotadas por Heracles;
f. listar las criaturas que no han sido derrotadas;
g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe o dios que la capturo;
h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de Erimanto indicando que Heracles las atrapó;
i. se debe permitir búsquedas por coincidencia;
j. eliminar al Basilisco y a las Sirenas;
k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles derroto a varias;
l. modifique el nombre de la criatura Ladón por Dragón Ladón;
m. realizar un listado por nivel del árbol;
n. muestre las criaturas capturadas por Heracles.
'''

from TDA_tree import BinaryTree
from ej23_lista_criaturas import lista_criaturas
from typing import Any

# --------- CREACIÓN DE FUNCIONES ADICIONALES --------- #

class BinaryTreeCriaturas(BinaryTree):

    def in_order_completo(self):
        def __in_order_completo(root):
            if root is not None:
                __in_order_completo(root.left)
                vencedor = root.other_values['derrotada_por']
                descripcion = root.other_values['descripcion']
                captor = root.other_values['capturada_por']
                print(f'  → Criatura: {root.value} | Descripción: {descripcion} | Derrotada por: {vencedor if vencedor else 'Nadie'} | Capturada por: {captor if captor else 'No capturada'}')
                __in_order_completo(root.right)

        if self.root is not None:
            __in_order_completo(self.root)

    # a. listado inorden de las criaturas y quienes la derrotaron;

    def listar_inorder(self):
        def __listar_inorder(root):
            if root is not None:
                __listar_inorder(root.left)
                print(f'  → Criatura: {root.value} | Derrotada por: {root.other_values['derrotada_por'] if root.other_values["derrotada_por"] else 'Nadie'}')
                __listar_inorder(root.right)

        if self.root is not None:
            __listar_inorder(self.root)

    # b. se debe permitir cargar una breve descripción sobre cada criatura;

    def cargar_descripcion(self, value: str, descripcion: Any):
        posicion = self.search(value)
        if posicion is None:
            return False
        else:
            posicion.other_values['descripcion'] = descripcion
            return True
        
    # d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;

    def determinar_mayores_vencedores(self):
        def __determinar_mayores_vencedores(root):
            if root is not None:
                __determinar_mayores_vencedores(root.left)
                vencedor = root.other_values['derrotada_por']
                if vencedor != '':
                    if vencedor in conteo:
                        conteo[vencedor] = conteo[vencedor] + 1
                    else:
                        conteo[vencedor] = 1
                __determinar_mayores_vencedores(root.right)

        conteo = {}
        if self.root is not None:
            __determinar_mayores_vencedores(self.root)

        pares = []
        for nombre, cantidad in conteo.items():
            pares.append((cantidad, nombre))
        pares_ordenados = sorted(pares, reverse=True)
        return pares_ordenados[:3]
    
    # e. listar las criaturas derrotadas por Heracles;

    def listar_por_vencedor(self, vencedor):
        def __listar_por_vencedor(root, vencedor):
            if root is not None:
                __listar_por_vencedor(root.left, vencedor)
                if root.other_values['derrotada_por'] == vencedor:
                    print(f'  → Criatura: {root.value} | Derrotada por: {root.other_values['derrotada_por']}')
                __listar_por_vencedor(root.right, vencedor)

        if self.root is not None:
            __listar_por_vencedor(self.root, vencedor)

    # f. listar las criaturas que no han sido derrotadas;

    def listar_no_derrotadas(self):
        def __listar_no_derrotadas(root):
            if root is not None:
                __listar_no_derrotadas(root.left)
                if root.other_values['derrotada_por'] == '':
                    print(f'  → {root.value}')
                __listar_no_derrotadas(root.right)

        if self.root is not None:
            __listar_no_derrotadas(self.root)

    # h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de Erimanto indicando que Heracles las atrapó;

    def modificar_capturada_por(self, value: str, captor: Any):
        posicion = self.search(value)
        if posicion is None:
            return False
        else:
            posicion.other_values['capturada_por'] = captor
            return True

    # i. se debe permitir búsquedas por coincidencia;

    def listar_por_coincidencia(self, coincidencia):
        def __listar_por_coincidencia(root, coincidencia):
            if root is not None:
                __listar_por_coincidencia(root.left, coincidencia)
                # if root.value.startswith(coincidencia) or coincidencia in root.value:
                if coincidencia in root.value:
                    print(f'  → {root.value}')
                __listar_por_coincidencia(root.right, coincidencia)

        if self.root is not None:
            __listar_por_coincidencia(self.root, coincidencia)

    # n. muestre las criaturas capturadas por Heracles.

    def mostrar_capturadas_por(self, captor):
        def __mostrar_capturadas_por(root, captor):
            if root is not None:
                __mostrar_capturadas_por(root.left, captor)
                if root.other_values['capturada_por'] == captor:
                    print(f'  → Criatura: {root.value} | Capturada por: {root.other_values['capturada_por']}')
                __mostrar_capturadas_por(root.right, captor)

        if self.root is not None:
            __mostrar_capturadas_por(self.root, captor)

# --------- CARGA DE DATOS --------- #

arbol_criaturas = BinaryTreeCriaturas()

for criatura in lista_criaturas:
    datos = {
        "nombre": criatura['nombre'],
        "derrotada_por": criatura['derrotada_por'],
        "descripcion": criatura['descripcion'],
        "capturada_por": criatura['capturada_por']
    }

    datos_copy = datos.copy()
    datos_copy.pop('nombre')
    arbol_criaturas.insert(criatura['nombre'], datos_copy)

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
print(f'\n{Color.CIAN}{f' EJERCICIO 23: CRIATURAS Y DIOSES '.center(140, "=")}{Color.RESET}')

# a. listado inorden de las criaturas y quienes la derrotaron;
print_seccion('a. listado inorden de las criaturas y quienes la derrotaron;')
print(f'{Color.AZUL}Listado:{Color.RESET}')
arbol_criaturas.listar_inorder()

# b. se debe permitir cargar una breve descripción sobre cada criatura; >> Ejemplo de muestra (no lo pide el ejercicio)
print_seccion('b. se debe permitir cargar una breve descripción sobre cada criatura;')
criatura_buscada = 'Tifón'
descripcion = 'Monstruo de cien cabezas.'
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
carga = arbol_criaturas.cargar_descripcion(criatura_buscada, descripcion)
if carga:
    print(f'  → El campo de la criatura {criatura_buscada} fue modificado correctamente.')
    print(f'  → Criatura: {criatura_buscada} | Decripción: {descripcion}')
else:
    print(f'  → No se pudo modificar el campo. {criatura_buscada} no se encuentra en el árbol.')

# c. mostrar toda la información de la criatura Talos;
print_seccion('c. mostrar toda la información de la criatura Talos;')
criatura_buscada = 'Talos'
posicion = arbol_criaturas.search(criatura_buscada)
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
if posicion is not None:
    vencedor = posicion.other_values['derrotada_por']
    descripcion = posicion.other_values['descripcion']
    captor = posicion.other_values['capturada_por']
    print(f'  → Criatura: {posicion.value} | Descripción: {descripcion} | Derrotada por: {vencedor} | Capturada por: {captor if captor else 'No capturada'}')
else:
    print(f'  → {criatura_buscada} no se encuentra en el árbol.')

# d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
print_seccion('d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;')
mayores_vencedores = arbol_criaturas.determinar_mayores_vencedores()
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
if mayores_vencedores:
    for vencedor in mayores_vencedores:
        print(f'  → Vencedor: {vencedor[1]} | Criaturas derrotadas: {vencedor[0]}')
else:
    print(f'  → No se encontraron vencedores.')

# e. listar las criaturas derrotadas por Heracles;
print_seccion('e. listar las criaturas derrotadas por Heracles;')
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
vencedor = 'Heracles'
arbol_criaturas.listar_por_vencedor(vencedor)

# f. listar las criaturas que no han sido derrotadas;
print_seccion('f. listar las criaturas que no han sido derrotadas;')
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
arbol_criaturas.listar_no_derrotadas()


# g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe o dios que la capturo;
print_seccion('g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe o dios que la capturo;')
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
print(f'  → Se agregó el campo "capturada_por" en la carga de datos.')

# h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de Erimanto indicando que Heracles las atrapó;
print_seccion('h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de Erimanto indicando que Heracles las atrapó;')
vencedor = 'Heracles'
print(f'{Color.VIOLETA}Resultados:{Color.RESET}')
criatura = 'Cerbero'
modificacion = arbol_criaturas.modificar_capturada_por(criatura, vencedor)
if modificacion:
    print(f'  → El campo de la criatura {criatura} fue modificado correctamente.')
else:
    print(f'  → No se pudo modificar el campo. {criatura} no se encuentra en el árbol.')

criatura = 'Toro de Creta'
modificacion = arbol_criaturas.modificar_capturada_por(criatura, vencedor)
if modificacion:
    print(f'  → El campo de la criatura {criatura} fue modificado correctamente.')
else:
    print(f'  → No se pudo modificar el campo. {criatura} no se encuentra en el árbol.')

criatura = 'Cierva de Cerinea'
modificacion = arbol_criaturas.modificar_capturada_por(criatura, vencedor)
if modificacion:
    print(f'  → El campo de la criatura {criatura} fue modificado correctamente.')
else:
    print(f'  → No se pudo modificar el campo. {criatura} no se encuentra en el árbol.')

criatura = 'Jabalí de Erimanto'
modificacion = arbol_criaturas.modificar_capturada_por(criatura, vencedor)
if modificacion:
    print(f'  → El campo de la criatura {criatura} fue modificado correctamente.')
else:
    print(f'  → No se pudo modificar el campo. {criatura} no se encuentra en el árbol.')

print(f'{Color.AZUL}\nListado actualizado:{Color.RESET}')
arbol_criaturas.in_order_completo()

# i. se debe permitir búsquedas por coincidencia;
print_seccion('i. se debe permitir búsquedas por coincidencia;')
print(f'{Color.AZUL}Coincidencia buscada:{Color.RESET}')
coincidencia = 'Jab'
print(f'  → {coincidencia}')
print(f'{Color.VIOLETA}\nResultado:{Color.RESET}')
arbol_criaturas.listar_por_coincidencia(coincidencia)

# j. eliminar al Basilisco y a las Sirenas;
print_seccion('j. eliminar al Basilisco y a las Sirenas;')
print(f'{Color.VIOLETA}Resultados:{Color.RESET}')
criatura_a_eliminar = 'Basilisco'
value, other_values = arbol_criaturas.delete(criatura_a_eliminar)
if value is not None:
    print(f'  → La criatura {criatura_a_eliminar} fue eliminada correctamente.')
else:
    print(f'  → La criatura {criatura_a_eliminar} no se encuentra en el árbol.')

criatura_a_eliminar = 'Sirenas'
value, other_values = arbol_criaturas.delete(criatura_a_eliminar)
if value is not None:
    print(f'  → La criatura {criatura_a_eliminar} fue eliminada correctamente.')
else:
    print(f'  → La criatura {criatura_a_eliminar} no se encuentra en el árbol.')

# k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles derroto a varias;
print_seccion('k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles derroto a varias;')
criatura = 'Aves del Estínfalo'
posicion = arbol_criaturas.search(criatura)
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
if posicion is not None:
    descripcion_original = posicion.other_values['descripcion']
    descripcion_nueva = f'{descripcion_original} Heracles derrotó a varias.'
    arbol_criaturas.cargar_descripcion(criatura, descripcion_nueva)
    print(f'  → Descripción actualizada correctamente.')
    print(f'  → Criatura: {posicion.value} | Descripción: {posicion.other_values['descripcion']}')
else:
    print(f'  → La criatura {criatura} no se encuentra en el árbol.')

# l. modifique el nombre de la criatura Ladón por Dragón Ladón;
print_seccion('l. modifique el nombre de la criatura Ladón por Dragón Ladón;')
criatura = 'Ladón'
posicion = arbol_criaturas.search(criatura)
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
if posicion is not None:
    value, other_values = arbol_criaturas.delete(criatura)
    new_value = 'Dragón Ladón'
    arbol_criaturas.insert(new_value, other_values)
    print(f'  → El nombre de la criatura fue actualizado correctamente.')
else:
    print(f'  → La criatura {criatura} no se encuentra en el árbol.')

print(f'{Color.AZUL}\nListado actualizado:{Color.RESET}')
arbol_criaturas.in_order_completo()

# m. realizar un listado por nivel del árbol;
print_seccion('m. realizar un listado por nivel del árbol;')
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
arbol_criaturas.by_level()

# n. muestre las criaturas capturadas por Heracles.
print_seccion('n. muestre las criaturas capturadas por Heracles.')
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
captor = 'Heracles'
arbol_criaturas.mostrar_capturadas_por(captor)

print(f'\n{Color.CIAN}{f" FIN DE EJECUCIÓN DEL PROGRAMA ".center(140, "=")}{Color.RESET}')
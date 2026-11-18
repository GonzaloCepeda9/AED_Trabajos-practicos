# 5. Topología de red en la universidad
'''
Cargar el esquema de red de la siguiente figura en un grafo e implementar los algoritmos necesarios para resolver las tareas, listadas a continuación:
a. cada nodo además del nombre del equipo deberá almacenar su tipo: pc, notebook, servidor, router, switch, impresora;
b. realizar un barrido en profundidad y amplitud partiendo desde la tres notebook: Red Hat, Debian, Arch;
c. encontrar el camino más corto para enviar a imprimir un documento desde la pc: Manjaro, Red Hat, Fedora hasta la impresora;
d. encontrar el árbol de expansión mínima;
e. determinar desde que pc (no notebook) es el camino más corto hasta el servidor “Guaraní”;
f. indicar desde que computadora del switch 01 es el camino más corto al servidor “MongoDB”;
g. cambiar la conexión de la impresora al router 02 y vuelva a resolver el punto b;
h. debe utilizar un grafo no dirigido.
'''

from ED_graph import Graph
from ED_list import List

# --------- CARGA DE DATOS --------- #

graph_network_topology = Graph(is_directed=False)

# VÉRTICES
graph_network_topology.insert_vertex('Switch 1', 'switch')
graph_network_topology.insert_vertex('Switch 2', 'switch')

graph_network_topology.insert_vertex('Router 1', 'router')
graph_network_topology.insert_vertex('Router 2', 'router')
graph_network_topology.insert_vertex('Router 3', 'router')

graph_network_topology.insert_vertex('Red Hat', 'notebook')
graph_network_topology.insert_vertex('Debian', 'notebook')
graph_network_topology.insert_vertex('Arch', 'notebook')

graph_network_topology.insert_vertex('Ubuntu', 'pc')
graph_network_topology.insert_vertex('Mint', 'pc')
graph_network_topology.insert_vertex('Manjaro', 'pc')
graph_network_topology.insert_vertex('Fedora', 'pc')
graph_network_topology.insert_vertex('Parrot', 'pc')

graph_network_topology.insert_vertex('Guaraní', 'servidor')
graph_network_topology.insert_vertex('MongoDB', 'servidor')

graph_network_topology.insert_vertex('Impresora', 'impresora')

# ARISTAS
# Conexiones de Switch 1
graph_network_topology.insert_edge('Switch 1', 'Debian', 17)
graph_network_topology.insert_edge('Switch 1', 'Ubuntu', 18)
graph_network_topology.insert_edge('Switch 1', 'Impresora', 22)
graph_network_topology.insert_edge('Switch 1', 'Mint', 80)
graph_network_topology.insert_edge('Switch 1', 'Router 1', 29)

# Conexiones de Router 1
graph_network_topology.insert_edge('Router 1', 'Router 2', 37)
graph_network_topology.insert_edge('Router 1', 'Router 3', 43)

# Conexiones de Router 2
graph_network_topology.insert_edge('Router 2', 'Red Hat', 25)
graph_network_topology.insert_edge('Router 2', 'Guaraní', 9)
graph_network_topology.insert_edge('Router 2', 'Router 3', 50)

# Conexiones de Router 3
graph_network_topology.insert_edge('Router 3', 'Switch 2', 61)

# Conexiones de Switch 2
graph_network_topology.insert_edge('Switch 2', 'Manjaro', 40)
graph_network_topology.insert_edge('Switch 2', 'Parrot', 12)
graph_network_topology.insert_edge('Switch 2', 'MongoDB', 5)
graph_network_topology.insert_edge('Switch 2', 'Fedora', 3)
graph_network_topology.insert_edge('Switch 2', 'Arch', 56)

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
print(f'\n{Color.CIAN}{f' EJERCICIO 5: TOPOLOGÍA DE RED EN LA UNIVERSIDAD '.center(140, "=")}{Color.RESET}')

# a. cada nodo además del nombre del equipo deberá almacenar su tipo: pc, notebook, servidor, router, switch, impresora;
print_seccion('a. cada nodo además del nombre del equipo deberá almacenar su tipo: pc, notebook, servidor, router, switch, impresora;')
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
print(f'\n{Color.AZUL}Ejemplos de muestra: {Color.RESET}')
for i in range(3):
    print(f'  → Equipo: {graph_network_topology[i].value} | Tipo: {graph_network_topology[i].other_values}')

# b. realizar un barrido en profundidad y amplitud partiendo desde la tres notebook: Red Hat, Debian, Arch;
print_seccion('b. realizar un barrido en profundidad y amplitud partiendo desde la tres notebook: Red Hat, Debian, Arch;')
notebooks = ['Red Hat', 'Debian', 'Arch']
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
for element in notebooks:
    print(f'\n{Color.AZUL}Barrido en profundidad desde {element}: {Color.RESET}')
    graph_network_topology.deep_sweep(element)
    print(f'\n{Color.AZUL}Barrido en amplitud desde {element}: {Color.RESET}')
    graph_network_topology.amplitude_sweep(element)

# c. encontrar el camino más corto para enviar a imprimir un documento desde la pc: Manjaro, Red Hat, Fedora hasta la impresora;
print_seccion('c. encontrar el camino más corto para enviar a imprimir un documento desde la pc: Manjaro, Red Hat, Fedora hasta la impresora;')
pcs = ['Manjaro', 'Red Hat', 'Fedora']
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
for element in pcs:
    path = graph_network_topology.dijkstra(element)
    destination = 'Impresora'
    peso_total = None
    camino_completo = List()

    # Reconstrucción del camino
    while path.size() > 0:
        value = path.pop()
        if value[0] == destination:
            if peso_total is None:
                peso_total = value[1]
            camino_completo.insert_value(value[0])
            destination = value[2]
    camino_completo.reverse()

    print(f'\n{Color.AZUL}Camino más corto desde {element} hasta la impresora es: {Color.RESET}')
    print(f'  → {" ——> ".join(camino_completo)}')
    print(f'  → Costo total: {peso_total}')
    
# d. encontrar el árbol de expansión mínima;
print_seccion('d. encontrar el árbol de expansión mínima;')
expansion_tree = graph_network_topology.kruskal('Switch 1')
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
print(f'\n{Color.AZUL}Árbol de expansión mínima: {Color.RESET}')
peso_total = 0
cantidad_aristas = 0
print(f'\n  Aristas: ')
for edge_str in expansion_tree.split(';'):
    origen, destino, peso = edge_str.split('-')
    print(f'  → {origen} ——> {destino} | Peso: {peso}')
    peso_total += int(peso)
    cantidad_aristas += 1

print(f'\n  Cantidad de aristas en el árbol: ')
print(f'  → {cantidad_aristas}.')
print(f'\n  Peso total del árbol: ')
print(f'  → {peso_total}.')

# e. determinar desde que pc (no notebook) es el camino más corto hasta el servidor “Guaraní”;
print_seccion('e. determinar desde que pc (no notebook) es el camino más corto hasta el servidor “Guaraní”;')
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')

pcs = ['Ubuntu', 'Mint', 'Manjaro', 'Fedora', 'Parrot']
destino = 'Guaraní'

mejor_pc = None
mejor_costo = float('inf')
mejor_camino = List()

for pc in pcs:
    path = graph_network_topology.dijkstra(pc)
    destino_actual = destino
    costo_actual = None
    camino_actual = List()
    
    while path.size() > 0:
        value = path.pop()
        if value[0] == destino_actual:
            if costo_actual is None:
                costo_actual = value[1]
            camino_actual.insert_value(value[0])
            destino_actual = value[2]
            
    camino_actual.reverse()
    
    if costo_actual < mejor_costo:
        mejor_costo = costo_actual
        mejor_pc = pc
        mejor_camino = camino_actual

print(f'\n{Color.AZUL}La PC con el camino más corto a Guaraní es:{Color.RESET}')
print(f'  → {mejor_pc}')
print(f'  → Camino: {" ——> ".join(mejor_camino)}')
print(f'  → Costo total: {mejor_costo}')

# f. indicar desde que computadora del switch 01 es el camino más corto al servidor “MongoDB”;
print_seccion('f. indicar desde que computadora del switch 01 es el camino más corto al servidor “MongoDB”;')
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')

computadoras_switch1 = ['Debian', 'Ubuntu', 'Mint']
destino_mongodb = 'MongoDB'

mejor_pc = None
mejor_costo = float('inf')
mejor_camino = List()

for pc in computadoras_switch1:
    path = graph_network_topology.dijkstra(pc)
    
    destino_actual = destino_mongodb
    costo_actual = None
    camino_actual = List()
    
    while path.size() > 0:
        value = path.pop()
        if value[0] == destino_actual:
            if costo_actual is None:
                costo_actual = value[1]
            camino_actual.insert_value(value[0])
            destino_actual = value[2]
            
    camino_actual.reverse()
    
    # Comparamos si este costo es menor al que teníamos guardado
    if costo_actual < mejor_costo:
        mejor_costo = costo_actual
        mejor_pc = pc
        mejor_camino = camino_actual

print(f'\n{Color.AZUL}La computadora del Switch 1 con el camino más corto a MongoDB es: {Color.RESET}')
print(f'  → {mejor_pc}')
print(f'  → Camino: {" ——> ".join(mejor_camino)}')
print(f'  → Costo total: {mejor_costo}')

# g. cambiar la conexión de la impresora al router 02 y vuelva a resolver el punto b;
print_seccion('g. cambiar la conexión de la impresora al router 02 y vuelva a resolver el punto b;')
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
graph_network_topology.delete_edge('value', 'Switch 1', 'Impresora')
graph_network_topology.insert_edge('Router 2', 'Impresora', 22)
notebook = ['Red Hat', 'Debian', 'Arch']

for element in notebook:
    print(f'\n{Color.AZUL}Barrido en profundidad desde {element}: {Color.RESET}')
    graph_network_topology.deep_sweep(element)
    
    print(f'\n{Color.AZUL}Barrido en amplitud desde {element}: {Color.RESET}')
    graph_network_topology.amplitude_sweep(element)

# h. debe utilizar un grafo no dirigido.
print_seccion('h. debe utilizar un grafo no dirigido.')
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
if not graph_network_topology.is_directed:
    print('  → El grafo es NO dirigido.')
else:
    print('  → El grafo es DIRIGIDO. Debe cambiarse a NO dirigido.')

print(f'\n{Color.CIAN}{f" FIN DE EJECUCIÓN DEL PROGRAMA ".center(140, "=")}{Color.RESET}')
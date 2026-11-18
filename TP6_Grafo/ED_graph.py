# Estructura de dato Grafo

from ED_list import List
from ED_queue import Queue
from ED_heap import HeapMin
from ED_stack import Stack
from typing import Any, Optional

class Graph(List):

    class __nodeVertex:

        def __init__(self, value: Any, other_values: Optional[Any] = None):
            self.value = value
            self.edges = List()
            self.edges.add_criterion('value', Graph._order_by_value)
            self.edges.add_criterion('weight', Graph._order_by_weight)
            self.other_values = other_values
            self.visited = False

        def __str__(self):
            return self.value

    class __nodeEdge:

        def __init__(self, value: Any, weight: Any, other_values: Optional[Any] = None):
            self.value = value
            self.weight = weight
            self.other_values = other_values # Aún no está en uso

        def __str__(self):
            return f'  → Destination: {self.value} | Weight: {self.weight}'

    def _order_by_value(item):
        return item.value

    def _order_by_weight(item):
        return item.weight

    def __init__(self, is_directed: bool = False):

        self.add_criterion('value', self._order_by_value)

        self.is_directed = is_directed

    def show(self) -> None:
        for vertex in self:
            print(f'Vertex: {vertex}')
            vertex.edges.show()

    def insert_vertex(self, value: Any, other_values: Any = None) -> None:
        node_vertex = Graph.__nodeVertex(value, other_values)
        self.insert_value(node_vertex)

    def insert_edge(self, origin_vertex: Any, destination_vertex: Any, weight: int) -> None:
        origin = self.search('value', origin_vertex)                                # Busco el vértice de origen para saber en la lista de quién agrego la arista.
        destination = self.search('value', destination_vertex)                      # Busco el vértice de destino para saber en la lista de quién agrego la arista (si el grafo es no dirigido).
        if origin is not None and destination is not None:                          # Si la búsqueda del "vértice origen NO es None" y la búsqueda del "vértice de destino NO es None", hago lo siguiente:
            node_edge_destination = Graph.__nodeEdge(destination_vertex, weight)    # Creo la variable "node_edge" que va a ser un "nodo arista" (una clase creada dentro del grafo), y se le pasa como parámetro el nombre del vértice de origen como value, y el peso como weight.
            self[origin].edges.insert_value(node_edge_destination)                  # Al vértice de origen buscado, en su lista de aristas, se le agrega el nuevo nodo arista creado.
            if not self.is_directed and origin != destination:                      # Si ese vértice de origen buscado es distinto al vértice de destino buscado, y el grafo SÍ es dirigido, hago lo siguiente:
                node_edge_origin = Graph.__nodeEdge(origin_vertex, weight)          # Creo la variable "node_edge" que va a ser un "nodo arista" (una clase creada dentro del grafo, y se le pasa como parámetro el nombre del vértice de origen como value, y el peso como weight.
                self[destination].edges.insert_value(node_edge_origin)              # Al vértice de destino buscado, en su lista de aristas, se le agrega el nuevo nodo arista creado.
        else:
            print('No se puede insertar. Falta al menos un vértice.')   # Este mensaje no debe ir acá. Modificar luego.

    def delete_edge(self, key_value: str, origin: Any, destination: Any) -> Optional[Any]:
        pos_origin = self.search(key_value, origin)
        if pos_origin is not None:
            edge = self[pos_origin].edges.delete_value(key_value, destination)
            if pos_origin is not None and not self.is_directed:
                pos_destination = self.search(key_value, destination)
                if pos_destination is not None:
                    self[pos_destination].edges.delete_value(key_value, origin)
            return edge

    def delete_vertex(self, value, key_value_vertex: str = None, key_value_edges: str = 'value'):
        delete_value = self.delete_value(key_value_vertex, value)
        if delete_value is not None:
            for vertex in self:
                self.delete_edge(key_value_edges, vertex.value, value)
        return delete_value

    def mark_as_unvisited(self) -> None:
        for vertex in self:
            vertex.visited = False

    def exist_path(self, origin, destination):
        def __exist_path(graph, origin, destination):
            result = False
            vertex_pos = graph.search('value', origin)
            if vertex_pos is not None:
                if not graph[vertex_pos].visited:
                    graph[vertex_pos].visited = True
                    if graph[vertex_pos].value == destination:
                        return True
                    for edge in graph[vertex_pos].edges:
                        destination_edge_pos = graph.search('value', edge.value)
                        if not graph[destination_edge_pos].visited:
                            result = __exist_path(graph, graph[destination_edge_pos].value, destination)
                            if result:
                                break
            return result

        self.mark_as_unvisited()
        result = __exist_path(self, origin, destination)
        return result

    def deep_sweep(self, value) -> None:
        def __deep_sweep(graph, value):
            pos_vertex = graph.search('value', value) # Si la busqueda de arista no se encuentra, falla y no ejecuta lo que está dentro del condicional.
            if pos_vertex is not None:
                if graph[pos_vertex].visited is False:
                    graph[pos_vertex].visited = True
                    print(f'  → {graph[pos_vertex]}')
                    for edge in graph[pos_vertex].edges:
                        pos_edge = graph.search('value', edge.value)
                        if graph[pos_edge].visited is False:
                            __deep_sweep(graph, graph[pos_edge].value)

        self.mark_as_unvisited()
        __deep_sweep(self, value)

    def amplitude_sweep(self, value) -> None:
        queue_vertex = Queue()
        self.mark_as_unvisited()
        vertex_pos = self.search('value', value)
        if vertex_pos is not None:
            self[vertex_pos].visited = True
            queue_vertex.arrive(self[vertex_pos])
            while queue_vertex.size() > 0:
                vertex = queue_vertex.attention()
                print(f'  → {vertex.value}')
                for edge in vertex.edges:
                    destination_edge_pos = self.search('value', edge.value)
                    if destination_edge_pos is not None:
                        if self[destination_edge_pos].visited is False:
                            self[destination_edge_pos].visited = True
                            queue_vertex.arrive(self[destination_edge_pos])

    def dijkstra(self, origin):
        from math import inf
        no_visited = HeapMin()
        path = Stack()
        for vertex in self:
            if vertex.value == origin:
                distance = 0
            else:
                distance = inf 
            no_visited.arrive([vertex.value, vertex, None], distance)
        
        while no_visited.size() > 0:
            value = no_visited.attention()
            costo_nodo_actual = value[0]

            path.push([value[1][0], costo_nodo_actual, value[1][2]])
            edges = value[1][1].edges

            for edge in edges:
                pos = no_visited.search(edge.value)
                
                if pos is not None:
                    if costo_nodo_actual + edge.weight < no_visited.elements[pos][0]:
                        no_visited.elements[pos][1][2] = value[1][0]                        
                        no_visited.change_priority(pos, costo_nodo_actual + edge.weight)
                        
        return path

    def kruskal(self, origin_vertex):
        def search_in_forest(forest, value):
            for index, tree in enumerate(forest):
                if value in tree:
                    return index
                
        forest = []
        edges = HeapMin()
        for vertex in self:
            forest.append(vertex.value)
            for edge in vertex.edges:
                edges.arrive([vertex.value, edge.value], edge.weight)
        
        while len(forest) > 1 and edges.size() > 0:
            edge = edges.attention()
            origin = search_in_forest(forest, edge[1][0])
            destination = search_in_forest(forest, edge[1][1])
            if origin is not None and destination is not None:
                if origin != destination:
                    if origin > destination:
                        vertex_origin = forest.pop(origin)
                        vertex_destination = forest.pop(destination)
                    else:
                        vertex_destination = forest.pop(destination)
                        vertex_origin = forest.pop(origin)


                    if '-' not in vertex_origin and '-' not in vertex_destination:
                        forest.append(f'{vertex_origin}-{vertex_destination}-{edge[0]}')
                    elif '-' not in vertex_destination:
                        forest.append(vertex_origin+';'+f'{edge[1][0]}-{vertex_destination}-{edge[0]}')
                    elif '-' not in vertex_origin:
                        forest.append(vertex_destination+';'+f'{vertex_origin}-{edge[1][1]}-{edge[0]}')
                    else:
                        forest.append(vertex_origin+';'+vertex_destination+';'+f'{edge[1][0]}-{edge[1][1]}-{edge[0]}')
        
        from_vertex = search_in_forest(forest, origin_vertex)

        if from_vertex is not None:
            return forest[from_vertex]
        else:
            return forest

    def es_adyacente(self, vertex, destination) -> bool:
        vertex_pos = self.search('value', vertex)
        if vertex_pos is not None:
            for edge in self[vertex_pos].edges:
                if edge.value == destination:
                    return True
        return False

    def adyacentes(self, vertex) -> None:
        vertex_pos = self.search('value', vertex)
        if vertex_pos is not None:
            for edge in self[vertex_pos].edges:
                print(edge.value)



    
# graph_letters = Graph(is_directed = True)

# graph_letters.insert_vertex('A')
# graph_letters.insert_vertex('B')
# graph_letters.insert_vertex('C')
# graph_letters.insert_vertex('D')
# graph_letters.insert_vertex('E')
# graph_letters.insert_vertex('F')

# graph_letters.insert_edge('A', 'B', 7)
# graph_letters.insert_edge('A', 'C', 5)
# graph_letters.insert_edge('A', 'D', 5)
# graph_letters.insert_edge('B', 'D', 4)
# graph_letters.insert_edge('B', 'E', 11)
# graph_letters.insert_edge('C', 'E', 18)
# graph_letters.insert_edge('C', 'F', 9)
# graph_letters.insert_edge('D', 'C', 2)
# graph_letters.insert_edge('E', 'F', 6)
# graph_letters.insert_edge('F', 'D', 1) 

# print(f'\n--------------------------- Es adyacente de... ---------------------------')
# print(f'¿A es adyacente de B? {graph_letters.es_adyacente("B", "A")}')
# print(f'¿B es adyacente de A? {graph_letters.es_adyacente("A", "B")}')
# print(f'¿F es adyacente de A? {graph_letters.es_adyacente("A", "F")}')
# print(f'¿A es adyacente de Z? {graph_letters.es_adyacente("Z", "A")}')

# print(f'\n--------------------------- Adyacentes de... ---------------------------')
# print('Adyacentes de A:')
# graph_letters.adyacentes('A')
# print('Adyacentes de F:')
# graph_letters.adyacentes('F')


# print(graph_letters.exist_path('A', 'C'))
    
# print('\n--------------------------- Borrar una arista ---------------------------')
# print(f'Grafo original: ')
# graph_letters.show()

# edge_origin = 'A'
# edge_destination = 'B'
# edge_deleted = graph_letters.delete_edge('value', edge_origin, edge_destination)

# if edge_deleted is not None:
#     print(f'\nLa arista {edge_origin} → {edge_destination} ha sido eliminada.')
#     if graph_letters.is_directed is False:
#         print(f'\nLa arista {edge_destination} → {edge_origin} ha sido eliminada.')
# else:
#     print(f'La arista {edge_origin} → {edge_destination} no se encuentra en el Grafo.')
# print(f'\nGrafo actualizado: ')
# graph_letters.show()

# print(f'\n--------------------------- Borrar un vértice ---------------------------')
# vertex_deleted = 'C'
# criterion_deleted = 'value'
# delete_value = graph_letters.delete_vertex(vertex_deleted, criterion_deleted)

# # print(f'\nTipo de dato de la variable "delete_value": {type(delete_value)}')
# # print(f'\nValor del vértice: {delete_value}')

# if delete_value is not None:
#     print(f'\nBorrando vértice {vertex_deleted} y sus aristas...')
#     print(f'\nGrafo actualizado: ')
#     graph_letters.show()
# else:
#     print(f'\nEl vértice {vertex_deleted} no se encuentra en el grafo.')

# print(f'\n--------------------------- Barrido en profundidad ---------------------------')
# graph_letters.mark_as_unvisited()
# graph_letters.deep_sweep('A')

# # print(graph_letters.exist_path('A', 'C'))

# print(f'\n--------------------------- Dijkstra ---------------------------')
# path = graph_letters.dijkstra('A')
# destination = 'E'
# peso_total = None
# camino_completo = []

# while path.size() > 0:
#     value = path.pop()
#     if value[0] == destination:
#         if peso_total is None:
#             peso_total = value[1]
#         camino_completo.append(value[0])
#         destination = value[2]
# camino_completo.reverse()
# print(f'El camino más corto es: {"-".join(camino_completo)} con un costo de {peso_total}')


# print(f'\n--------------------------- Kruskal ---------------------------')

# # Grafo NO dirigido para Kruskal
# graph_kruskal = Graph(is_directed=False)

# graph_kruskal.insert_vertex('A')
# graph_kruskal.insert_vertex('B')
# graph_kruskal.insert_vertex('C')
# graph_kruskal.insert_vertex('D')
# graph_kruskal.insert_vertex('E')
# graph_kruskal.insert_vertex('F')

# graph_kruskal.insert_edge('A', 'B', 7)
# graph_kruskal.insert_edge('A', 'C', 5)
# graph_kruskal.insert_edge('A', 'D', 5)
# graph_kruskal.insert_edge('B', 'D', 4)
# graph_kruskal.insert_edge('B', 'E', 11)
# graph_kruskal.insert_edge('C', 'E', 18)
# graph_kruskal.insert_edge('C', 'F', 9)
# graph_kruskal.insert_edge('D', 'C', 2)
# graph_kruskal.insert_edge('E', 'F', 6)
# graph_kruskal.insert_edge('F', 'D', 1)

# expansion_tree = graph_kruskal.kruskal('A')
# print(f'Árbol de expansión mínimo: {expansion_tree}')

# peso_total = 0
# cantidad_aristas = 0
# for edge in expansion_tree.split(';'):
#     origin, destination, weight = edge.split('-')
#     print(f'  Arista {origin} - {destination} | Peso: {weight}')
#     peso_total += int(weight)
#     cantidad_aristas += 1

# print(f'Cantidad de aristas: {cantidad_aristas} (esperado: 5 = n - 1)')
# print(f'Peso total: {peso_total} (esperado: 18)')
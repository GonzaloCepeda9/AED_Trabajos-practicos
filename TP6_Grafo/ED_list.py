# Estructura de dato Lista

from typing import Any, Optional

class List(list):

    CRITERION_FUNCTIONS = {}

    def add_criterion(self, key_criterion: str, function):
        self.CRITERION_FUNCTIONS[key_criterion] = function # Sintaxis para agregar clave-valor a un diccionario: diccionario[clave] = valor

    def insert_value(self, value: Any) -> None:
        self.append(value)

    def delete_value(self, key_value: str, value) -> Optional[Any]:
        position = self.search(key_value, value)
        # return self.pop(position) if position is not None else position
        if position is not None:
            return self.pop(position)
        else:
            return position

    def is_empty(self):
        if self:
            return False
        else:
            return True

    def search(self, search_key: str, search_value) -> int:

        # Búsqueda binaria
        self.sort_by_criterion(search_key)
        criterion = self.CRITERION_FUNCTIONS.get(search_key)
        if criterion is None and self and not isinstance(self[0], (int, str, bool)):
            return None
        start = 0
        end = len(self) -1
        middle = (start + end) // 2

        while start <= end:
            value = criterion(self[middle]) if criterion else self[middle] # Si hay criterio se ejecuta la función; si no, se pasa el dato directamente.
            if value == search_value:
                return middle
            elif value < search_value:
                start = middle + 1
            elif value > search_value:
                end = middle - 1   
            middle = (start + end) // 2

        return None
        
    def sort_by_criterion(self, criterion_key: str = None) -> None:

        criterion = self.CRITERION_FUNCTIONS.get(criterion_key)
        
        if criterion is not None:
            self.sort(key=criterion)
        elif self and isinstance(self[0], (int, str, bool)):
            self.sort()
        else:
            print(f'\nCriterio de orden no encontrado.')

    def size(self):
        return len(self)

    def show(self):
        for element in self:
            print(element)
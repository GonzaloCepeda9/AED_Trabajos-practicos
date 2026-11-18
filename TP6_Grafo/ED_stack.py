# Estructura de dato Pila

from typing import Any, Optional

class Stack:

    def __init__(self):
        self.__elements = []

    def push(self, value: Any) -> None:
        self.__elements.append(value)

    def pop(self) -> Optional[Any]:
        if self.__elements:
            return self.__elements.pop()
        else:
            None
        
    def size(self) -> int:
        return len(self.__elements)

    def on_top(self) -> Optional[Any]:
        if self.__elements:
            return self.__elements[-1]
        else:
            return None

    def is_empty(self):
        if self.__elements:
            return False
        else:
            return True
        
    def show(self):
        aux_stack = Stack()
        while self.size() > 0:
            value = self.pop()
            print(value)
            aux_stack.push(value)

        while aux_stack.size() > 0:
            self.push(aux_stack.pop())
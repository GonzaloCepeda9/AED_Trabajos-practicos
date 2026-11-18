# Estructura de dato Cola

from typing import Any, Optional

class Queue:
    
    def __init__(self):
        self.__elements = []

    def arrive(self, value: Any) -> None:
        self.__elements.append(value)

    def attention(self) -> Optional[Any]:
        # Versión estándar:
        if self.__elements:
            return self.__elements.pop(0)
        else:
            return None
        
        # # Versión opcional acortada:
        # return (
        #     self.__elements(0)
        #     if self.__elements|
        #     else None
        # )

    def on_front(self) -> Optional[Any]:
        if self.__elements:
            return self.__elements[0]
        else:
            return None
        
    def size(self) -> int:
        return len(self.__elements)
    
    def move_to_end(self) -> Optional[Any]:
        if self.__elements:
            value = self.attention()
            self.arrive(value)
            return value
        else:
            return None
        
    def is_empty(self):
        if self.__elements:
            return False
        else:
            return True
    
    def show(self):
        for _ in range(self.size()):
            value = self.move_to_end()
            print(value)
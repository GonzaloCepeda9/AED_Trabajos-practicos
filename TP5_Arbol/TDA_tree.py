from TDA_queue import Queue
from typing import Any, Optional

class BinaryTree:

    class __nodeTree:

        def __init__(self, value: Any, other_values: Optional[Any] = None):
            self.value = value
            self.other_values = other_values
            self.left = None
            self.right = None
            self.height = 0

    def __init__(self):
        self.root = None

    def insert(self, value: Any, other_values: Optional[Any] = None):
        def __insert(root, value, other_values):
            if root is None:
                nodo = BinaryTree.__nodeTree(value, other_values)
                return nodo
            elif value < root.value:
                root.left = __insert(root.left, value, other_values)
            else:
                root.right = __insert(root.right, value, other_values)

            root = self.auto_balance(root)
            self.update_height(root)
            return root

        self.root = __insert(self.root, value, other_values)

    def in_order(self):
        def __in_order(root):
            if root is not None:
                __in_order(root.left)
                print(f'  → {root.value}')
                __in_order(root.right)

        if self.root is not None:
            __in_order(self.root)

    def post_order(self):
        def __post_order(root):
            if root is not None:
                __post_order(root.right)
                print(f'  → {root.value}')
                __post_order(root.left)

        if self.root is not None:    
            __post_order(self.root)

    def pre_order(self):
            def __pre_order(root):
                if root is not None:
                    print(f'  → {root.value}')
                    __pre_order(root.left)
                    __pre_order(root.right)

            if self.root is not None:
                __pre_order(self.root)

    def by_level(self):
        tree_queue = Queue()
        if self.root is not None:
            tree_queue.arrive(self.root)

            while tree_queue.size() > 0:
                node = tree_queue.attention()
                print(f'  → {node.value}') 
                if node.left is not None:
                    tree_queue.arrive(node.left)
                if node.right is not None:
                    tree_queue.arrive(node.right)

    def search(self, value: Any) -> __nodeTree:
        def __search(root, value):
            if root is not None:
                if value == root.value:
                    return root
                elif value < root.value:
                    return __search(root.left, value)
                else:
                    return __search(root.right, value)
        aux = None
        if self.root is not None:
            aux = __search(self.root, value)
        return aux

    def proximity_search(self, value: Any) -> __nodeTree:
        def __search(root, value):
            if root is not None:
                if root.value.startswith(value):
                    print(root.value)
                __search(root.left, value)
                __search(root.right, value)

        aux = None
        if self.root is not None:
            aux = __search(self.root, value)
        return aux

    def delete(self, value):
        
        def __replace(root):

            if root.right is None:
                return root.left, root
            else:
                root.right, replace_node = __replace(root.right)
                root = self.auto_balance(root)
                self.update_height(root)
                return root, replace_node

        def __delete(root, value):

            deleted_value = None
            deleted_other_values = None

            if root is None:
                return None, None, None
            
            if value < root.value:
                root.left, deleted_value, deleted_other_values = __delete(root.left, value)

            elif value > root.value:
                root.right, deleted_value, deleted_other_values = __delete(root.right, value)

            else:
                deleted_value = root.value
                deleted_other_values = root.other_values

                if root.left is None and root.right is None:
                    return None, deleted_value, deleted_other_values

                elif root.left is None:
                    return root.right, deleted_value, deleted_other_values
                
                elif root.right is None:
                    return root.left, deleted_value, deleted_other_values
                
                else:
                    root.left, replace_node = __replace(root.left)
                    root.value = replace_node.value
                    root.other_values = replace_node.other_values

            if root is not None:
                root = self.auto_balance(root)
                self.update_height(root)
            
            return root, deleted_value, deleted_other_values

        deleted_value = None
        deleted_other_values = None

        if self.root is not None:
            self.root, deleted_value, deleted_other_values = __delete(self.root, value)

        return deleted_value, deleted_other_values

    def height(self, root):
        if root is None:
            return -1
        else:
            return root.height

    def update_height(self, root):
        if root is not None:
            alt_left = self.height(root.left)
            alt_right = self.height(root.right)
            root.height = max(alt_left, alt_right) + 1

    def simple_rotation(self, root, control):
        if control:
            aux = root.left
            root.left = aux.right
            aux.right = root
        else:
            aux = root.right
            root.right = aux.left
            aux.left = root

        self.update_height(root)
        self.update_height(aux)
        return aux

    def double_rotation(self, root, control):
        if control:
            root.left = self.simple_rotation(root.left, False)
            root = self.simple_rotation(root, True)
        else:
            root.right = self.simple_rotation(root.right, True)
            root = self.simple_rotation(root, False)
        return root

    def auto_balance(self, root):
        if root is not None:
            if self.height(root.left) - self.height(root.right) == 2:
                control = True
                if self.height(root.left.left) >= self.height(root.left.right):
                    root = self.simple_rotation(root, control)
                else:
                    root = self.double_rotation(root, control)
            elif self.height(root.right) - self.height(root.left) == 2:
                control = False
                if self.height(root.right.right) >= self.height(root.right.left):
                    root = self.simple_rotation(root, control)
                else:
                    root = self.double_rotation(root, control)
        return root

    def divide_tree(self, arbol_v, arbol_f, condition):
        def __divide_tree(root, arbol_v, arbol_f, condition):
            if root is not None:
                if root.other_values[condition] is True:
                    arbol_v.insert(root.value, root.other_values)
                else:
                    arbol_f.insert(root.value, root.other_values)
                __divide_tree(root.left, arbol_v, arbol_f, condition)
                __divide_tree(root.right, arbol_v, arbol_f, condition)

        __divide_tree(self.root, arbol_v, arbol_f, condition)
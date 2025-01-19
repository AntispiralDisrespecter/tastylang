
from .symbol_table import SymbolTable

class Node(dict):

    def __init__(self, **kwargs):
        if "type" not in kwargs:
            raise Exception("Node must have a type")
        super().__init__(**kwargs)

class AST(list):

    def __init__(self, nodes=None):
        if nodes is None:
            pass

    def push(self, node):
        if not isinstance(node, Node):
            raise Exception(f"Expected Node, got {type(node)}")
        self.append(node)

    def peek(self):
        return self[-1]

        

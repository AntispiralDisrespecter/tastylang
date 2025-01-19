

class Scope(dict):

    def __init__(self, parent=None):
        self.parent = parent

class SymbolTable:

    def __init__(self):
        self.scopes = [Scope()]

    def define(self, name, value):
        self.scopes[-1][name] = value

    def resolve(self, name):
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]
        raise NameError(name)
    
    def pushScope(self):
        self.scopes.append(Scope(self.scopes[-1]))

    def popScope(self):
        if self.scopes[-1].parent is None:
            raise RuntimeError("Cannot pop the global scope")
        self.scopes.pop()
    


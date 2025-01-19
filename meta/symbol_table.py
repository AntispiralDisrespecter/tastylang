
class Scope(dict):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.parent = kwargs["parent"]

class GlobalScope(Scope):

    def __init__(self, **kwargs):
        kwargs["parent"] = None
        super().__init__(**kwargs)

class SymbolTable:

    def __init__(self):
        self.scopes = [GlobalScope()]

    def __repr__(self):
        return f"{self.scopes!r}"
    
    def peek(self):
        return self.scopes[-1]

    def define(self, name, value):
        self.scopes[-1][name] = value

    def resolve(self, name):
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]
        return None
    
    def pushScope(self):
        self.scopes.append(Scope(parent=self.peek()))

    def popScope(self):
        if isinstance(self.peek(), GlobalScope):
            raise RuntimeError("Cannot pop the global scope")
    

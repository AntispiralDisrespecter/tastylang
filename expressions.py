
class Expression:

    def __init__(self):
        pass

    def __repr__(self):
        return "Expression()"
        
class Var(Expression):

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Var({self.name})"

class Lambda(Expression):

    def __init__(self, arg, body):
        self.arg = arg
        self.body = body

    def __repr__(self):
        return f"Lambda({self.arg}, {self.body!r})"

class Application(Expression):

    def __init__(self, func, arg):
        self.func = func
        self.arg = arg

    def __repr__(self):
        return f"Application({self.func!r}, {self.arg!r})"


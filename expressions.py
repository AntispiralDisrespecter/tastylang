
class MetaType(type):
    
    def __repr__(cls):
        return f"<class '{cls.__module__}.{cls.__name__}'>"

class Expression(metaclass=MetaType):

    def __init__(self):
        if type(self) is Expression:
            raise TypeError(f"CANNOT CALL ABSTRACT CLASS {self.__class__.__name__}")

    def __repr__(self):
        return "Expression()"

        
class Var(Expression):

    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError(f"NAME {name} MUST BE {str}, GOT {type(name)}")
        self.name = name

    def __repr__(self):
        return f"Var({self.name})"

class Lambda(Expression):

    def __init__(self, arg, body):
        if not isinstance(arg, Var):
            raise TypeError(f"ARGUMENT {arg} MUST BE {Var}, GOT {type(arg)}")
        if not isinstance(body, Expression):
            raise TypeError(f"BODY {body} MUST BE {Expression}, GOT {type(body)}")
        self.arg = arg
        self.body = body

    def __repr__(self):
        return f"Lambda({self.arg}, {self.body!r})"

class Application(Expression):

    def __init__(self, func, arg):
        if not isinstance(func, Var):
            raise TypeError(f"FUNCTION {func} MUST BE {Var}, GOT {type(func)}")
        if not isinstance(arg, Expression):
            raise TypeError(f"ARGUMENT {arg} MUST BE {Expression}, GOT {type(arg)}")
        self.func = func
        self.arg = arg

    def __repr__(self):
        return f"Application({self.func!r}, {self.arg!r})"

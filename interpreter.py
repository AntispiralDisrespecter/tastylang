

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

class AST:

    def __init__(self, string):
        self.string = string
        self.parse()

    def __repr__(self):
        return f"{self.expression!r}"

    def parse(self):
        stack = []
        for idx,ch in enumerate(self.string):
            if ch == "~":
                arg = stack.pop()
                body = stack.pop()
                exp = Lambda(arg, body)
            elif ch == "@":
                func = stack.pop()
                arg = stack.pop()
                exp = Application(func, arg)
            else:
                exp = Var(ch)
            stack.append(exp)
        if len(stack) == 1:
            self.expression = stack.pop()
        else:
            raise ValueError("INVALID EXPRESION")

class Value:

    def __init__(self):
        pass

class ChurchNumeral(Value):

    def __init__(self, ast):
        self.exp = ast.expression
        self.evaluate()

    def __repr__(self):
        return self.val

    def evaluate(self):
        l1 = self.exp
        if not isinstance(l1, Lambda):
            raise ValueError(f"Expected Lambda. Got {type(l1)}")
        l2 = l1.body
        if not isinstance(l1, Lambda):
            raise ValueError(f"Expected Lambda. Got {type(l2)}")
        body = l2.body
        if isinstance(body, Var):
            self.val = 0
            return
        if not isinstance(body, Application):
            raise ValueError(f"Expected Application. Got {type(body)}")
        curr, count = body, 0
        while isinstance(curr, Application):
            curr = curr.arg
            count += 1
        if not isinstance(curr, Var):
            raise ValueError(f"Expected Var. Got {type(body)}")
        self.val = count



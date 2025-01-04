

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

    def expectLambda(self, exp):
        if not isinstance(exp, Lambda):
            raise ValueError(f"Expected Lambda. Got {type(exp)}")
        return exp

    def expectApplication(self, exp):
        if not isinstance(exp, Application):
            raise ValueError(f"Expected Application. Got {type(exp)}")
        return exp

    def expectVar(self, exp):
        if not isinstance(exp, Var):
            raise ValueError(f"Expected Var. Got {type(exp)}")
        return exp

    def evaluate(self):
        l1 = self.expectLambda(self.exp)
        l2 = self.expectLambda(l1.body)
        if isinstance(l2.body, Var):
            self.val = 0
            return
        body = self.expectApplication(l2.body)
        curr, count = body, 0
        while isinstance(curr, Application):
            curr = curr.arg
            count += 1
        self.expectVar(curr)
        self.val = count


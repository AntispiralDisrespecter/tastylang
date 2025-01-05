
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

class ASTError(Exception):
    
    def __init__(self, message):
        super().__init__(f"{type(self).__name__}: {message}")

class AST:

    def __init__(self, string):
        self.string = string
        self.parse()

    def __repr__(self):
        return f"{self.expression!r}"

    def parse(self):

        def pop2(stack):
            try:
                return stack.pop(), stack.pop()
            except IndexError as e:
                raise ASTError("INVALID EXPRESSION")

        stack = []
        for idx,ch in enumerate(self.string):
            if ch == "~":
                arg, body = pop2(stack)
                exp = Lambda(arg, body)
            elif ch == "@":
                func, arg = pop2(stack)
                exp = Application(func, arg)
            else:
                exp = Var(ch)
            stack.append(exp)
        if len(stack) == 1:
            self.expression = stack.pop()
        else:
            raise ASTError("INVALID EXPRESION")

class Value:

    def __init__(self, ast):
        self.exp = ast.expression

    def __repr__(self):
        if isinstance(self.exp, Value):
            return self.exp.name
        tokens = []

class ChurchNumeralError(Exception):
    
    def __init__(self, message):
        super().__init__(f"{type(self).__name__}: {message}")

class ChurchNumeral(Value):

    def __init__(self, ast):
        self.exp = ast.expression
        self.evaluate()

    def __repr__(self):
        return str(self.val)

    def expectLambda(self, exp):
        if not isinstance(exp, Lambda):
            raise ChurchNumeralError(f"Expected Lambda. Got {type(exp).__name__}.")
        return exp

    def expectApplication(self, exp):
        if not isinstance(exp, Application):
            raise ChurchNumeralError(f"Expected Application. Got {type(exp).__name__}.")
        return exp

    def expectVar(self, exp):
        if not isinstance(exp, Var):
            raise ChurchNumeralError(f"Expected Var. Got {type(exp).__name__}.")
        return exp

    def assertNameMatch(self, var1, var2):
        if var1.name != var2.name:
            raise ChurchNumeralError(f"Names {var1!r}, {var2!r} must match.")

    def evaluate(self):
        l1 = self.expectLambda(self.exp)
        l2, v1 = self.expectLambda(l1.body), self.expectVar(l1.arg)
        if isinstance(l2.body, Var):
            self.assertNameMatch(l2.body, l2.arg)
            self.val = 0
            return
        body, v2 = self.expectApplication(l2.body), self.expectVar(l2.arg)
        curr, count = body, 0
        while isinstance(curr, Application):
            func = self.expectVar(curr.func)
            self.assertNameMatch(v1, func)
            curr = curr.arg
            count += 1
        v3 = self.expectVar(curr)
        self.assertNameMatch(v2, v3)
        self.val = count

class Interpreter:

    def __init__(self):
        pass

    def parse(self, string):
        try:
            return AST(string)
        except ASTError as e:
            print(e)

    def evaluate(self, ast):
        try:
            return ChurchNumeral(ast)
        except ChurchNumeralError as e:
            print(e)

    def run(self, string):
        ast = self.parse(string)
        if ast is not None:
            val = self.evaluate(ast)
            if val is not None:
                return val


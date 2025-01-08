
from expressions import Expression, Var, Lambda, Application

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


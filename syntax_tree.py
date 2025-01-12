
from expressions import Expression, Var, Lambda, Application

class ASTError(Exception):
    
    def __init__(self, message):
        super().__init__(f"{type(self).__name__}: {message}")

class AST:

    def __init__(self, string, reduce=False):
        self.string = string
        self.parse()
        if reduce:
            self.expression = self.reduce()

    def __repr__(self):
        return f"{self.expression!r}"

    def fromAST(self, ast, reduce=False):
        self.string = ast.string
        self.expression = ast.expression
        if reduce:
            self.expression = self.reduce()

    def reduce(self, exp=None):

        def isReduced(exp):
            if isinstance(exp, Application):
                if not isinstance(exp.func, Var):
                    return False
            return True

        def substitute(left, right):
            if isinstance(left.body, Var):
                if left.arg.name == left.body.name:
                    return right
            elif isinstance(left.body, Lambda):
                if left.arg.name == left.body.arg.name:
                    return left.body
            raise ASTError("BETA REDUCTION FAILED") 

        if not exp:
            exp = self.expression
        if isReduced(exp):
            return exp
        if isinstance(exp.func, Lambda):
            return substitute(exp.func, exp.arg)
        if isinstance(exp.func, Application):
            return substitute(self.reduce(exp.func), exp.arg)
        raise ASTError("BETA REDUCTION FAILED")

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
    

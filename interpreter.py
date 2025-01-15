
from evaluation import Value, Identity, ChurchNumeral
from evaluation import EvalError, IdentityError, ChurchNumeralError
from syntax_tree import AST, ASTError

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
            pass

        try:
            return Identity(ast)
        except IdentityError as e:
            pass

        return Value(ast)

    def run(self, string):
        ast = self.parse(string)
        if ast is not None:
            val = self.evaluate(ast)
            if val is not None:
                return val


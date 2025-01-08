
from expressions import Expression, Var, Lambda, Application
from syntax_tree import AST

class EvalError(Exception):
    
    def __init__(self, message):
        super().__init__(f"{type(self).__name__}: {message}")

class ChurchNumeralError(EvalError):
    
    def __init__(self, message):
        pass

class IdentityError(EvalError):

    def __init__(self, message):
        pass

class Value:

    def __init__(self, ast, error=EvalError):
        self.exp = ast.expression
        self.Error = error

    def __repr__(self):
        return f"{self.exp!r}"

    def expectLambda(self, exp):
        if not isinstance(exp, Lambda):
            raise self.Error(f"Expected Lambda. Got {type(exp).__name__}.")
        return exp

    def expectApplication(self, exp):
        if not isinstance(exp, Application):
            raise self.Error(f"Expected Application. Got {type(exp).__name__}.")
        return exp

    def expectVar(self, exp):
        if not isinstance(exp, Var):
            raise self.Error(f"Expected Var. Got {type(exp).__name__}.")
        return exp

    def assertNameMatch(self, var1, var2):
        if var1.name != var2.name:
            raise self.Error(f"Names {var1!r}, {var2!r} must match.")

    def reduce(self):
        pass    

class Identity(Value):
    
    def __init__(self, ast):
        super().__init__(ast, IdentityError)
        self.evaluate()

    def __repr__(self):
        return str(self.val)

    def evaluate(self):
        l1 = self.expectLambda(self.exp)
        v1, v2 = self.expectVar(l1.arg), self.expectVar(l1.body)
        self.assertNameMatch(v1, v2)
        self.val = "Id"


class ChurchNumeral(Value):

    def __init__(self, ast):
        super().__init__(ast, ChurchNumeralError)
        self.evaluate()

    def __repr__(self):
        return str(self.val)

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


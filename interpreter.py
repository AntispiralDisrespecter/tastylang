
class TastyLambda:

    def __init__(self, func, name="lambda", freevars=()):
        self.func = func
        self.name = name
        self.freevars = freevars

    def __repr__(self):
        return f"{self.name}: <closure> [captures: {self.freevars}]"

def application(stack):
    f1, f2 = stack.pop(), stack.pop()
    stack.append(f2.func(f1))

def closure(stack):
    f1, f2 = stack.pop(), stack.pop()
    f = lambda x : f1.func(f2.func(x))
    freevars = (f1.name, f2.name)
    tl = TastyLambda(
        f,
        name="closure",
        freevars=freevars
    )
    stack.append(tl)

OPERATORS = {
    "@" : lambda x : application(x),
    "~" : lambda x : closure(x)
}

def evaluate(exp):
    tokens = list(exp)
    stack = []
    while len(tokens):
        token = tokens.pop(0)
        if token in OPERATORS:
            OPERATORS[token](stack)
        else:
            tl = TastyLambda(lambda x:x, token)
            stack.append(tl)
    if len(stack) == 1:
        return stack.pop()
    raise ValueError("INVALID EXPRESSION")

def runREPL():
    print("Tasty REPL. Type 'exit' or (CTRL+D) to quit")
    while True:
        try:
            exp = input(">> ").strip()
        except EOFError as e:
            print()
            break
        if not len(exp):
            continue
        elif exp == "exit":
            break
        try:
            res = evaluate(exp)
            print(res)
        except ValueError as e:
            print(e)


#print(TastyLambda(lambda x : lambda y : x + y).func.__code__.co_freevars)
           
runREPL()


# Wrapper class for lambda expressions. Functional units are called 'tastys'
# and are composed together using functional application and closure.
class TastyLambda:

    def __init__(self, func=None, name="lambda", freevars=()):
        self.func = func
        self.name = name
        self.freevars = freevars

    def __repr__(self):
        if "closure_" in self.name:
            return f"{self.name}: <closure> [captures: {self.freevars}]"
        elif "application_" in self.name:
            return f"{self.name}: <application> []"
        else:
            return f"{self.name}: <primitive> []"

# Wrapper class for ENV variables and lexical items
class Environment:

    def __init__(self):
        self.env = {
            "CLOSURE_COUNT": 0,
            "APPLICATION_COUNT": 0
        }

    def reset(self):
        self.env = {
            "CLOSURE_COUNT": 0,
            "APPLICATION_COUNT": 0
        }
    
    def show(self):
        for k,v in self.env.items():
            print(f"{k}: {v}")

# Factory function for application Tastys
def application(stack):
    
    def getNextName():
        env.env["APPLICATION_COUNT"] += 1
        count = env.env["APPLICATION_COUNT"]
        return f"application_{count}"

    f1, f2 = stack.pop(), stack.pop()
    f = lambda x : lambda y : x(y)
    name = getNextName()
    tl = TastyLambda(f, name, ())
    stack.append(tl)
    env.env[tl.name] = tl

# Factory function for closure Tastys 
def closure(stack):

    def getNextName():
        env.env["CLOSURE_COUNT"] += 1
        count = env.env["CLOSURE_COUNT"]
        return f"closure_{count}"

    f1, f2 = stack.pop(), stack.pop()
    if f1.name == f2.name:
        f = lambda x : x
        name = "identity"
        freevars=(f1.name)
    else:
        f = lambda x : f2
        name = getNextName()
        freevars = (f2.name)
            
    tl = TastyLambda(f, name, freevars)
    stack.append(tl)
    env.env[tl.name] = tl

# These are the only two operators in the lexicon and
# can be used perform any Turing complete computation
# with simple stack based interpretation.
OPERATORS = {
    "@" : lambda x : application(x),
    "~" : lambda x : closure(x)
}

# Bug fix -- decoder not covering all valid computations
# Need to tweak this for human readable output
def decode(tasty):
    try:
        while True:
            if isinstance(tasty, int):
                return tasty
            tasty = tasty.func(lambda x: x+1).func(0)
    except Exception as e:
        print(e)
        return tasty

# A simple stack based interpreter takes advantage of reverse 
# polish notation to make parsing trivially easy with
# unambigous lexical scope. No parentheses or delimiters
# are needed.
def evaluate(exp):
    tokens = list(exp)
    stack = []
    while len(tokens):
        token = tokens.pop(0)
        if token in OPERATORS:
            OPERATORS[token](stack)
        else:
            if token not in env.env:
                env.env[token] = TastyLambda(name=token)
            stack.append(env.env[token])
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
        if exp == "exit":
            break
        if exp == "show":
            env.show()
            continue
        if exp == "reset":
            env.reset()
            continue
        try:
            func = evaluate(exp)
            print(decode(func))
        except ValueError as e:
            print(e)


env = Environment()
runREPL()

# Test cases for valid expressions
# The first case encodes the identity function
# The next two are syntactically valid but cannot be fully evaluated out of context
# The last three cases encode 0, 1, and 2 as Church numerals
# Need to fix decoder to make outputs human readable
'''
print(evaluate("aa~"))
print(evaluate("ab~"))
print(evaluate("ab~c~"))
print(evaluate("aa~b~"))
print(evaluate("ab@a~b~"))
print(evaluate("ab@b@a~b~"))
'''

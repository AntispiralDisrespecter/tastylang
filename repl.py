
from interpreter import AST, ASTError, ChurchNumeral, ChurchNumeralError

def parse(string):
    try:
        return AST(string)
    except ASTError as e:
        print(e)

def evaluate(ast):
    try:
        return ChurchNumeral(ast)
    except ChurchNumeralError as e:
        print(e)

def runInterpreter(string):
    ast = parse(string)
    if ast is not None:
        val = evaluate(ast)
        if val is not None:
            print(val)   

def runREPL():
    print("Tasty REPL. Type 'exit' or (CTRL^D) to quit.")
    while True:
        try:
            string = input(">> ").strip()
        except EOFError:
            print()
            break
        match string:
            case "":
                continue
            case "exit":
                break
            case _:
                runInterpreter(string)

if __name__ == "__main__":
    runREPL()
             

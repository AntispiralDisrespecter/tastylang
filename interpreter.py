
def evaluate(exp):
    return exp 

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
            
runREPL()


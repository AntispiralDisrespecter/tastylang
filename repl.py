
from interpreter import Interpreter

def runREPL():
    interpreter = Interpreter()
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
                res = interpreter.run(string)
                print(res)

if __name__ == "__main__":
    runREPL()
             

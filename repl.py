
from interpreter import AST, ASTError, ChurchNumeral, ChurchNumeralError

def run():
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
                try:
                    print(ChurchNumeral(AST(string)))
                except (ASTError, ChurchNumeralError) as e:
                    print(e)
                    

if __name__ == "__main__":
    run()
             

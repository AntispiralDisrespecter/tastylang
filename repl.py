
from interpreter import Interpreter
from modes import user, debug


class REPLError(Exception):

    def __init__(self, message):
        super().__init__(f"{type(self).__name__}: {message}")
        
class REPL:

    def __init__(self, **modes):
        self.modes = modes
        if "user" not in self.modes:
            self.modes["user"] = user
        if "debug" not in self.modes:
            self.modes["debug"] = debug
        self.currMode = self.modes["user"]
        self.interpreter = Interpreter()

    def setMode(self, modeName):
        self.currMode = self.modes[modeName]

    def exitMode(self):
        match self.currMode.name:
            case "user":
                exit()
            case _:
                self.setMode("user")

    def eval(self, string):
        match self.currMode.name:
            case "user":
                return self.interpreter.run(string)
            case "debug":
                return eval(string)
            case _:
                raise REPLError(f"NO RUNTIME ENV FOR {self.currMode.name}")

    def run(self):
        print("Tasty REPL. Type 'exit' or (CTRL^D) to quit.")
        while True:
            try:
                string = input(self.currMode.prompt).strip()
            except EOFError:
                print()
                break
            match string:
                case "":
                    continue
                case "exit":
                    self.exitMode()
                case "debug":
                    self.setMode("debug")
                case _:
                    res = self.eval(string)
                    print(res)

if __name__ == "__main__":
    repl = REPL()
    repl.run()
             

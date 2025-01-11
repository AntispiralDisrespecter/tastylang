
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
        self.history = []

    def setMode(self, modeName):
        self.currMode = self.modes[modeName]

    def exitMode(self):
        match self.currMode.name:
            case "user":
                exit()
            case _:
                self.setMode("user")

    def pushHistory(self, command):
        self.history.append(command)

    def showHistory(self):
        for idx,command in enumerate(self.history):
            print(f"{idx}: {command}")

    def eval(self, string):
        match self.currMode.name:
            case "user":
                return self.interpreter.run(string)
            case "debug":
                try:
                    return eval(string, {}, debug.env)
                except Exception as e:
                    return e
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
                case "history":
                    self.showHistory()
                case "debug":
                    self.setMode("debug")
                case _:
                    res = self.eval(string)
                    print(res)
            self.history.append(string)

if __name__ == "__main__":
    repl = REPL()
    repl.run()
             

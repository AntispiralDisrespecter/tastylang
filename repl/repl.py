
import sys

from core.interpreter import Interpreter as Core
from meta.interpreter import Interpreter as Meta
from .modes import user, debug

class REPLError(Exception):

    def __init__(self, message):
        super().__init__(f"{type(self).__name__}: {message}")
        
class REPL:

    def __init__(self, interpreter, **modes):
        self.modes = modes
        if "user" not in self.modes:
            self.modes["user"] = user
        if "debug" not in self.modes:
            self.modes["debug"] = debug
        self.currMode = self.modes["user"]
        self.interpreter = Core() if interpreter == "core" else Meta()
        self.history = []

    def setMode(self, modeName):
        self.currMode = self.modes[modeName]
        debug.env["history"] = []

    def exitMode(self):
        match self.currMode.name:
            case "user":
                exit()
            case _:
                self.setMode("user")

    def pushHistory(self, command):
        match self.currMode.name:
            case "user":
                self.history.append(command)
            case "debug":
                debug.env["history"].append(command)
                
    def showHistory(self):
        match self.currMode.name:
            case "user":
                history = self.history
            case "debug":
                history = debug.env["history"]

        for idx,command in enumerate(history):
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
                    if res is not None:
                        return res
                    self.pushHistory(string)

             

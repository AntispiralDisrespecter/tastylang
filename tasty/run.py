import sys
from core.interpreter import Interpreter as Core
from meta.interpreter import Interpreter as Meta
from repl import REPL

def runREPL(interpreter):
    if interpreter not in ["core", "meta"]:
        print("Usage: tasty [core|meta] [file.tasty]")
        sys.exit(1)
    repl = REPL(interpreter)
    repl.run()

def runFile(interpreter, file):
    if interpreter not in ["core", "meta"]:
        print("Usage: tasty [core|meta] [file.tasty]")
        sys.exit(1)
    with open(file) as f:
        program = f.read()
    runtime = Core() if interpreter == "core" else Meta()
    runtime.run(program)

def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ["core", "meta"]:
        print("Usage: tasty [core|meta] [file.tasty]")
        sys.exit(1)

    interpreter = sys.argv[1]
    file = sys.argv[2] if len(sys.argv) == 3 else None
    if file is not None:
        runFile(interpreter, file)
    else:
        runREPL(interpreter)

if __name__ == "__main__":
    main()

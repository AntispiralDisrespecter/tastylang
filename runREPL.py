import sys
from repl import REPL

if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in ["core", "meta"]:
        print("Usage: python runRepl.py [core|meta]")
        sys.exit(1)

    repl = REPL(sys.argv[1])
    repl.run()

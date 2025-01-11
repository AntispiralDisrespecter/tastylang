
from syntax_tree import AST
from expressions import Expression, Var, Lambda, Application
from evaluation import ChurchNumeral, Identity

class Mode:

    def __init__(self, name, prompt, env=None):
        self.name = name
        self.prompt = prompt
        self.env = env

user = Mode("user", ">> ")
debug = Mode("debug", "[debug] >> ",
    env = {
        "AST": AST,
        "Expression": Expression,
        "Var": Var,
        "Lambda": Lambda,
        "Application": Application,
        "ChurchNumeral": ChurchNumeral,
        "Identity": Identity
    }
)


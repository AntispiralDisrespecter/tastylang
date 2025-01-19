
from core.syntax_tree import AST
from core.expressions import Expression, Var, Lambda, Application
from core.evaluation import ChurchNumeral, Identity

class Mode:

    def __init__(self, name, prompt, env=None):
        self.name = name
        self.prompt = prompt
        self.env = env

user = Mode("user", ">> ")
meta = Mode("meta", ">> ")
debug = Mode("debug", "[debug] >> ",
    env = {
        "AST": AST,
        "Expression": Expression,
        "Var": Var,
        "Lambda": Lambda,
        "Application": Application,
        "ChurchNumeral": ChurchNumeral,
        "Identity": Identity,
        "history": []
    }
)


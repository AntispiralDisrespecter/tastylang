
class Mode:

    def __init__(self, name, prompt):
        self.name = name
        self.prompt = prompt

user = Mode("user", ">> ")
debug = Mode("debug", "[debug] >> ")


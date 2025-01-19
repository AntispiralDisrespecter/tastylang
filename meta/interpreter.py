from .symbol_table import SymbolTable
from .syntax_tree import Node, AST

class Interpreter:

    def __init__(self):
        self.symbolTable = SymbolTable()

    def run(self, string):
        return self.eagerEval(string)

    def eagerEval(self, program):
        ast = self.parseProgram(program)
        for node in ast:
            res = self.evaluateNode(node)
            if res is not None:
                return res

    def parseProgram(self, program):
        ast = AST()
        for statement in program.splitlines():
            node = self.parseStatement(statement)
            if node:
                ast.push(node)
        return ast

    def evaluateNode(self, node):
        node_type = node["type"]
        if node_type == "assign":
            self.symbolTable.define(node["name"], node["value"])
        elif node_type == "print":
            print(self.symbolTable.resolve(node["name"]))
        elif node_type == "return":
            return self.symbolTable.resolve(node["name"])
        else:
            raise Exception(f"Unknown node: {node}")

    def parseStatement(self, statement):
        if not statement.strip():
            return None
        if statement.startswith("let"):
            return self.parseAssignment(statement)
        if statement.startswith("print"):
            return self.parsePrint(statement)
        if statement.startswith("return"):
            return self.parseReturn(statement)
        raise Exception(f"Unknown statement: {statement}")

    def parseAssignment(self, statement):
        try:
            _, name, value = statement.split(maxsplit=2)
            name = name.strip()
            value = value.split('=', maxsplit=1)[1].strip()
            return Node(type="assign", name=name, value=value)
        except ValueError:
            raise Exception(f"Invalid assignment: {statement}")

    def parsePrint(self, statement):
        try:
            _, name = statement.split(maxsplit=1)
            name = name.strip()
            value = self.symbolTable.resolve(name)
            return Node(type="print", name=name, value=value)
        except ValueError:
            raise Exception(f"Invalid print: {statement}")

    def parseReturn(self, statement):
        try:
            _, name = statement.split(maxsplit=1)
            name = name.strip()
            value = self.symbolTable.resolve(name)
            return Node(type="return", name=name, value=value)
        except ValueError:
            raise Exception(f"Invalid return: {statement}")


import unittest

from expressions import Expression, Var, Lambda, Application
from syntax_tree import AST, ASTError
from evaluation import  ChurchNumeral, ChurchNumeralError, Identity, IdentityError
from interpreter import Interpreter

class TestEvaluate(unittest.TestCase):

    def test_0(self):
        self.assertEqual(ChurchNumeral(AST("aa~b~")).val, 0)

    def test_1(self):
        self.assertEqual(ChurchNumeral(AST("ab@a~b~")).val, 1)

    def test_2(self):
        self.assertEqual(ChurchNumeral(AST("ab@b@a~b~")).val, 2)

    def test_3(self):
        self.assertEqual(ChurchNumeral(AST("ab@b@b@a~b~")).val, 3)

    def test_id_a(self):
        self.assertEqual(Identity(AST("aa~")).val, "Id")

    def test_invalid_ast_a(self):
        try:
            AST("")
        except ASTError:
            pass

    def test_invalid_church_a(self):
        try:
            ChurchNumeral(AST("aa~"))
        except ChurchNumeralError:
            pass

    def test_invalid_church_b(self):
        try:
            ChurchNumeral(AST("ab@"))
        except ChurchNumeralError:
            pass

    def test_interpreter_a(self):
        val = Interpreter().run("aa~b~")
        self.assertEqual(val.val, 0)

if __name__ == "__main__":
    unittest.main()

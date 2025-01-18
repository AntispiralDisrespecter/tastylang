
import unittest

from core.syntax_tree import AST, ASTError

class TestBetaReduce(unittest.TestCase):

    # Reduce Id(Id)
    def test_a(self):
        self.assertEqual(AST("aa~bb~@").getReduce(), AST("aa~"))
   
    # Reduce Id(Id)(Id)
    def test_b(self):
        self.assertEqual(AST("aa~bb~cc~@@").getReduce(), AST("aa~"))

    # Reduce Id(Id(Id))
    def test_c(self):
        self.assertEqual(AST("aa~bb~@cc~@").getReduce(), AST("aa~"))

    # Reduce Id(0)
    def test_d(self):
        self.assertEqual(AST("ab@a~b~cc~@").getReduce(), AST("ab@a~b~"))

if __name__ == "__main__":
    unittest.main()

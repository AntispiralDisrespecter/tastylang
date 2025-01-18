
import unittest

from syntax_tree import AST, ASTError

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

if __name__ == "__main__":
    unittest.main()

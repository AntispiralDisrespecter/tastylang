
import unittest

from interpreter import AST, ChurchNumeral

class TestEvaluate(unittest.TestCase):

    def test_0(self):
        self.assertEqual(ChurchNumeral(AST("aa~b~")).val, 0)

    def test_1(self):
        self.assertEqual(ChurchNumeral(AST("ab@a~b~")).val, 1)

    def test_2(self):
        self.assertEqual(ChurchNumeral(AST("ab@b@a~b~")).val, 2)

    def test_3(self):
        self.assertEqual(ChurchNumeral(AST("ab@b@b@a~b~")).val, 3)

if __name__ == "__main__":
    unittest.main()

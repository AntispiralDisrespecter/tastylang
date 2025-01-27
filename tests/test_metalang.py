
import unittest, os, glob

from meta.interpreter import Interpreter as Meta
from core.interpreter import Interpreter as Core

class TestMetalang(unittest.TestCase):

    def setUp(self):
        self.meta = Meta()
        self.meta.attach(Core())
        self.programsDir = os.path.join(os.path.dirname(__file__), "./programs/meta/")
        self.tastyFiles = glob.glob(self.programsDir + "input/*.tasty")
        self.txtFiles = glob.glob(self.programsDir + "gold/*.txt")
        
    def test_programs(self):
        for tasty, txt in zip(self.tastyFiles, self.txtFiles):
            with open(tasty, "r") as tastyFile:
                program = tastyFile.read()
                with open(txt, "r") as txtFile:
                    expected = txtFile.read().strip()
                    res = self.meta.eagerEval(program)
                    self.assertEqual(res.__repr__(), expected)


if __name__ == "__main__":
    unittest.main()


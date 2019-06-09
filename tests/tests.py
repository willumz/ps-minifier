import unittest
import os
import ps_minifier.psminifier as psmin

class TestMinifiedOutput(unittest.TestCase):

    def test_equals(self):
        self.assertRegex(psmin.main(["psminifier.py"], file='$a = "b"'), '^\$[a-z]="b"$')
        self.assertRegex(psmin.main(["psminifier.py"], file='$a   = "b"'), '^\$[a-z]="b"$')
        self.assertRegex(psmin.main(["psminifier.py"], file='$a =    "b"'), '^\$[a-z]="b"$')
    
    def test_genVars(self):
        # Test 1 char
        psmin.variables[0] = ""
        psmin.genVars()
        for i in psmin.variables:
            self.assertRegex(i, '^[a-zA-Z]$')
        self.assertEqual(len(psmin.variables), len(set(psmin.variables)))
        
        # Test 2 chars
        psmin.variables[0] = "a"
        psmin.genVars()
        for i in psmin.variables:
            self.assertRegex(i, '^[a-zA-Z][a-zA-Z0-9]$')
        self.assertEqual(len(psmin.variables), len(set(psmin.variables)))
    
    def test_getVar(self):
        psmin.variable = psmin.variables[0]
        psmin.var_count = 0
        self.assertEqual(psmin.variables[psmin.var_count], psmin.getVar())
        self.assertRegex(psmin.getVar(), "^[a-zA-Z][a-zA-Z0-9]*$")
    
    def test_string_integrity(self):
        self.assertRegex(psmin.main(["psminifier.py"], file='$a = "hello there!"'), '^\$[a-z]="hello there!"$')


if __name__ == '__main__':
    unittest.main()
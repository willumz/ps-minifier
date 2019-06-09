import unittest
import os
import ps_minifier.psminifier as psmin

class TestMinifiedOutput(unittest.TestCase):

    def test_equals(self):
        self.assertRegex(psmin.main(["psminifier.py"], file='$a = "b"'), '^\$[a-z]="b"$')
        self.assertRegex(psmin.main(["psminifier.py"], file='$a   = "b"'), '^\$[a-z]="b"$')
        self.assertRegex(psmin.main(["psminifier.py"], file='$a =    "b"'), '^\$[a-z]="b"$')

if __name__ == '__main__':
    unittest.main()
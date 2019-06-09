import unittest
import ps_minifier.psminifier as psmin

class TestMinifiedOutput(unittest.TestCase):

    def test_equals(self):
        self.assertEqual(psmin.main(["psminifier.py"], file='$a = "b"'), '$a="b"')
        self.assertEqual(psmin.main(["psminifier.py"], file='$a   = "b"'), '$a="b"')
        self.assertEqual(psmin.main(["psminifier.py"], file='$a =    "b"'), '$a="b"')

if __name__ == '__main__':
    unittest.main()
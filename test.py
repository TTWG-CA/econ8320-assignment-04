import unittest
from complex import ComplexNumber

class TestComNum(unittest.TestCase):
    
    def test_ne(self):
        self.assertNotEqual(ComplexNumber(4,3), ComplexNumber(4,-3))
        

unittest.main(argv=[''], verbosity=2, exit=False)
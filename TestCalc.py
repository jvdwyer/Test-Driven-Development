import unittest
import Calc

class TestLeet(unittest.TestCase):

    def test_add(self):
        self.assertEquals(Calc.add(10, 5), 15)
        self.assertEquals(Calc.add(-1, 1), 0)
        self.assertEquals(Calc.add(-1, -1), -2)
    
    def test_subtract(self):
        self.assertEquals(Calc.subtract(10, 5), 5)
        self.assertEquals(Calc.subtract(-1, 1), -2)
        self.assertEquals(Calc.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEquals(Calc.multiply(10, 5), 50)
        self.assertEquals(Calc.multiply(-1, 1), -1)
        self.assertEquals(Calc.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEquals(Calc.divide(10, 5), 2)
        self.assertEquals(Calc.divide(-1, 1), -1)
        self.assertEquals(Calc.divide(-1, -1), 1)
        self.assertEquals(Calc.divide(5, 2), 2.5)

        with self.assertRaises(ValueError):
            Calc.divide(10, 0)
    

if __name__ == '__main__':
    unittest.main()

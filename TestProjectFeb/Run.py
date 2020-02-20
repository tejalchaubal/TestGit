import unittest
import Calc

class TestCalc(unittest.TestCase):
    def test_add(self):
        result=Calc.add(5,5)
        self.assertEqual(result,10)
        print(result)
if __name__=='__main__':
    unittest.main()


from fractions import Fraction  # My first add to the test file

import unittest
from my_sum import sum  # Import function from package

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """Test that it can sum a list of integers"""
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)  # Expected output is 6
 
def test_list_fraction(self):          # My second add lines 13-19 to the test file
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, 1)   # My second add lines 13-19 to the 


if __name__ == '__main__':
    unittest.main()

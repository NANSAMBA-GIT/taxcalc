import unittest

class taxcalc(unittest.TestCase):
    def test_first_test(self):
        self.assertEqual(taxcalculation(800,12), 0.0)
        self.assertEqual(taxcalculation(2000,12), 400.0)
        self.assertEqual(taxcalculation(9000,12), 3600.0)

if __name__== "__main__":
    unittest.main()
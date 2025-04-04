import unittest

def taxcalculation(earning, months):
    if not isinstance(earning, (int, float)) or not isinstance(months, (int, float)):
        raise ValueError ("both earning and months must be numeric")
    if isinstance (earning, (str)) or isinstance(months, (str)):
        raise ValueError ("strings can't be entered as earning or months")
    if earning <= 0 or months <= 0:
        raise ValueError ("earning and months can't be negative")
    if earning < 1000:
        return 0.0
    elif earning < 3000:
        return earning*0.2*months
    else:
        return earning*0.4*months

class taxcalc(unittest.TestCase):
    def test_first_test(self):
        self.assertEqual(taxcalculation(800,12), 0.0)

    def test_second_test(self):
        self.assertEqual(taxcalculation(2000,12), 4800.0)

    def test_third_test(self):
        self.assertEqual(taxcalculation(9000,12), 43200.0)


if __name__== "__main__":
    unittest.main()
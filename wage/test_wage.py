import unittest
from wage import computepay


class TestWage(unittest.TestCase):

    def test_computepay(self):
        self.assertEqual(computepay(10, 10), 100)
        self.assertEqual(computepay(41, 10), 415)
        self.assertEqual(computepay(40, 0), 0)
        self.assertNotEqual(computepay(40, 0), 7)

        with self.assertRaises(ValueError):
            computepay(-3, 56)


if __name__ == '__main__':
    unittest.main()

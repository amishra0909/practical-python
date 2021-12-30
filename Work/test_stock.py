# test_stock.py

import unittest
import stock


class TestStock(unittest.TestCase):

    def test_create(self):
        s = stock.Stock('IBM', 75, 91.1)
        self.assertEqual(s.name, 'IBM')
        self.assertEqual(s.shares, 75)
        self.assertEqual(s.price, 91.1)

    def test_cost(self):
        s = stock.Stock('GOOG', 100, 490.10)
        self.assertEqual(s.cost, 49010)

    def test_sell(self):
        s = stock.Stock('GOOG', 100, 490.10)
        s.sell(25)
        self.assertEqual(s.shares, 75)

    def test_setting_shares_to_not_int(self):
        s = stock.Stock('GOOG', 100, 490.10)
        with self.assertRaises(TypeError):
            s.shares = '100'


if __name__ == '__main__':
    unittest.main()

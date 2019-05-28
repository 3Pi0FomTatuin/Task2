import unittest
import lib


class MyTestCase(unittest.TestCase):
    converter = lib.Converter()

    def test_zero(self):
        self.assertEqual(self.converter.number_to_words('0'), 'zero')

    def test_ones(self):
        self.assertEqual(self.converter.number_to_words('5'), 'five')

    def test_teens(self):
        self.assertEqual(self.converter.number_to_words('13'), 'thirteen')

    def test_composite(self):
        self.assertEqual(self.converter.number_to_words('25'), 'twenty-five')

    def test_and(self):
        self.assertEqual(self.converter.number_to_words('2025'), 'two thousand and twenty-five')

    def test_mill(self):
        self.assertEqual(self.converter.number_to_words('1002025'), 'one million, two thousand and twenty-five')


if __name__ == '__main__':
    unittest.main()

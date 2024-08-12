import unittest

from main import suma

class TestSuma(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(suma(1, 2), 3)

if __name__ == '__main__':
    unittest.main()
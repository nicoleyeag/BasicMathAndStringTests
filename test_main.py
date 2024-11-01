import unittest
from main import add, reverse_string, is_even

class TestBasicFunctions(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-2, 3), 1)
        self.assertEqual(add(-10, -5), -15)

    def test_revstr(self):
        self.assertEqual(reverse_string('potato'), 'otatop')
        self.assertEqual(reverse_string('coffee'), 'eeffoc')
        self.assertEqual(reverse_string(''), '')

if __name__ == '__main__':
    unittest.main()

import unittest

from main import add, reverse_string, is_even

class TestBasicFunctions(unittest.TestCase):

    def add_test(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-2, 3), 1)
        self.assertEqual(add(-10, -5), 15)
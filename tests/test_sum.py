import unittest
from sum import add

"""Test file"""


class TestAdd(unittest.TestCase):
    """
            To test the 'add' function
    """
    def test_add(self):
        result = add(5, 7)
        self.assertEqual(result, 12)


if __name__ == '__main__':
    unittest.main()

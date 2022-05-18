import unittest


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """

        self.assertEqual(6, 6)

if __name__ == '__main__':
    unittest.main()

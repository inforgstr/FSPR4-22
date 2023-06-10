import unittest

from random_game import find_num


class TestRandomGame(unittest.TestCase):
    def test_correct_guess(self):
        """Test for correct value (when its returns True)"""
        test_value = 3
        guess = 3

        result = find_num(test_value, guess)
        self.assertTrue(result)

    def test_correct_numeric_guess(self):
        """Test when guess given as numeric in string (returns True)"""
        test_value = 3
        guess = "3"

        result = find_num(test_value, guess)
        self.assertTrue(result)

    def test_incorrect_guess(self):
        """Test for incorrect value (when its returns None)"""
        test_value = 4
        guess = 1

        result = find_num(test_value, guess)
        self.assertIsNone(result)

    def test_incorrect_numeric_guess(self):
        """Test when gues given as numeric in string (returns False)"""
        test_value = 5
        guess = "3"

        result = find_num(test_value, guess)
        self.assertIsNone(result)

    def test_out_range_guess(self):
        """Test when guess out of range (returns False)"""
        test_value = 10
        guess = 11

        result = find_num(test_value, guess)
        self.assertFalse(result)

    def test_non_numeric_guess(self):
        """Test when guess given as ascii value (returns exception ValueError)"""
        test_value = 5
        guess = "ABC"

        result = find_num(test_value, guess)
        self.assertIsInstance(result, ValueError)


if __name__ == "__main__":
    unittest.main()

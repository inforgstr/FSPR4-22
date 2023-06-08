import unittest

import lesson_29


class TestLesson29(unittest.TestCase):
    def test_mainPlus(self):
        test_num = 10
        result = lesson_29.plus(test_num)
        # Checking equals
        self.assertEqual(result, 15)

    def test_strPlus(self):
        test_name = "1asdf"
        result = lesson_29.plus(test_name)
        self.assertIsInstance(result, ValueError)

    def test_lessPlus(self):
        test_name = -1
        result = lesson_29.plus(test_name)
        self.assertEqual(result, "Wrong argument were given!")

    def test_emptyPlus(self):
        test_name = 0
        result = lesson_29.plus(test_name)
        self.assertEqual(result, "Wrong argument were given!")
        
    

if __name__ == "__main__":
    unittest.main()

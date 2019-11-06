import unittest
from simple_exp import cap_text


class TestCap(unittest.TestCase):

    # Pass
    def test_one_word(self):
        text = 'python'
        result = cap_text(text)
        self.assertEqual(result, 'Python')

    # Pass
    def test_multiple_words(self):
        text = 'python rocks'
        result = cap_text(text)
        self.assertEqual(result, 'Python Rocks')

    # Fail
    def test_with_apostrophes(self):
        text = "python rock's flying colors"
        result = cap_text(text)
        self.assertEqual(result, "Python Rock's Flying Colors")


if __name__ == '__main__':
    unittest.main()
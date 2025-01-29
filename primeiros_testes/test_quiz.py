import unittest
from quiz import quiz, questions

class TestQuiz(unittest.TestCase):

    def test_all_correct_answers(self):
        user_answers = ["B", "A", "B", "A", "D"]
        with unittest.mock.patch('builtins.input', side_effect=user_answers):
            score = quiz(questions)
            self.assertEqual(score, 5)

    def test_all_incorrect_answers(self):
        user_answers = ["A", "B", "C", "D", "A"]
        with unittest.mock.patch('builtins.input', side_effect=user_answers):
            score = quiz(questions)
            self.assertEqual(score, 0)

    def test_some_correct_answers(self):
        user_answers = ["B", "B", "B", "A", "A"]
        with unittest.mock.patch('builtins.input', side_effect=user_answers):
            score = quiz(questions)
            self.assertEqual(score, 3)

    def test_invalid_answers(self):
        user_answers = ["E", "B", "A", "X", "D", "C", "B", "A", "D"]
        with unittest.mock.patch('builtins.input', side_effect=user_answers):
            score = quiz(questions)
            self.assertEqual(score, 4)

if __name__ == '__main__':
    unittest.main()
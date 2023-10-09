from unittest import TestCase
import triple_list_exercise


class TestTripleListExercise(TestCase):
    def test_triple_list_exercise(self):

        numbers = [3, 7, 2, 6, 5]

        self.assertEqual(triple_list_exercise.triple_list_exercise(numbers),[27, 343, 8, 216, 125])













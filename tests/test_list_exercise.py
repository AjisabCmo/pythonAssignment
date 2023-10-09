from unittest import TestCase
import list_exercise

class TestListExercise(TestCase):
    def test_add_function_exist(self):
        list_exercise.add_function([15,20,25,20,10,5])
    def test_add_function(self):
        self.assertEqual(list_exercise.add_function([15,20,25,20,10,5]),95)

    def test_multiply_function(self):
        self.assertEqual(list_exercise.multiply_function([15,20,25,20,10,5]),7500000)

    def test_largest_function(self):
        self.assertEqual(list_exercise.largest_function([15,20,25,20,10,5]),25)

    def test_smallest_function(self):
        self.assertEqual(list_exercise.smallest_function([15,20,25,20,10,5]),5)

    def test_duplicate_function(self):
        result=[15,20,25,10,5]
        ans = list_exercise.duplicate_function([15,20,25,20,10,5])
        self.assertEqual(ans,[15,20,25,10,5])
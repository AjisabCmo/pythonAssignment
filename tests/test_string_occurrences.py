from unittest import TestCase
import class_task



class TestStringOccurrences(TestCase):
    def test_string_occurrences(self):
        self.assertEqual(class_task.string_occurrences("restart"),"resta$t")
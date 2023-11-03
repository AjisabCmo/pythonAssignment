from unittest import TestCase
import weekend_task

class TestWeekendTask(TestCase):
    def test_my_function_remove_string(self):
        sample_input = ['', 'ABC', 'xyz', '', 'abc', 'XYZ']
        result =['ABC', 'xyz', 'abc', 'XYZ']
        self.assertEqual(weekend_task.remove_string(sample_input),result)
from unittest import TestCase
import task


class TestTask(TestCase):

    def test_biggest_odd(self):
        self.assertEqual(task.biggest_odd('23495'),9)
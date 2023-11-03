from unittest import TestCase
import work_hard

class TestAddIng(TestCase):
    def test_add_ing(self):
        sample_input='abc'
        sample_output='abcing'
        self.assertEqual(work_hard.add_ing(sample_input),sample_output)

    def test_add_ing(self):
        sample_input='sting'
        sample_output = 'stingly'
        self.assertEqual(work_hard.add_ly(sample_input),sample_output)

    def test_add_it(self):
        sample_input='it'
        sample_output='it'
        self.assertEqual(work_hard.add_it(sample_input),sample_output)
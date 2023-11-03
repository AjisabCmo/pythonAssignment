from unittest import TestCase
import assignment

class TestCornFlakes(TestCase):
    def test_list_to_dictionary_func(self):
        actual = assignment.list_to_dictionary(['apple', 'banana', 'coconut'])
        expected = {'a': 'apple', 'b': 'banana', 'c': 'coconut'}
        self.assertEqual(actual,expected)

    def test_for_same_character_func(self):
        actual = assignment.list_to_dic_same(['apple', 'banana', 'coconut','corn'])
        expected = {'a': 'apple', 'b': 'banana', 'c': 'coconut', 'C': 'corn'}
        self.assertEqual(actual,expected)

    def test_two_list_dictionary_func(self):
        input1 = ['a', 'b', 'c' ,'d', 'e']
        input2 = [1, 2, 3, 4, 5]
        sample_outputs = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
        self.assertEqual(assignment.two_list_dictionary(input1,input2),sample_outputs)

    def test_largest_smallest_list(self):
        sample_list = [10, 75, 20, 30, 15, 5, 40, 25, 40, 35]
        sample_output = 70
        self.assertEqual(assignment.largestsmallestlist(sample_list),sample_output)

    def test_frequency_greaterthan_any_value(self):
        sample_input = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 5, 5, 5, 6, 7]
        sample_output = [1, 2, 5]
        self.assertEqual(assignment.frequency_greater_than_value_func(sample_input),sample_output)

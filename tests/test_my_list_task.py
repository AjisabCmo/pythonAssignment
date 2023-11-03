from unittest import TestCase
import my_list_task

class TestMyListTask(TestCase):
    def test_my_list_function_exist(self):
        result=list(range(1,21))
        self.assertEqual(my_list_task.exercise1(),result)
    def test_oddNumber_function(self):
        list1=list(range(1,21))

        result = list(range(1,21,2))
        self.assertEqual(my_list_task.oddNumber_function(list1),result)

    def test_double_oddNumber_function(self):
        list1=list(range(1,21))
        result=[2,6,10,14,18,22,26,30,34,38]
        self.assertEqual(my_list_task.doubleOddNumber(list1),result)

    def test_element_between_index_4_and_7(self):
        list1=list(range(1,21))
        result=[2,6,10,14,0,0,0,0,34,38]
        self.assertEqual(my_list_task.indexfourandseventoZero(list1),result)

    def test_function_can_concatenate_two_list(self):
        list1=['w','a','th','xplo']
        list2=['e','re','e','rers']

        list3=['we','are','the','xplorers']
        self.assertEqual(my_list_task.concatenate(list1, list2), list3)
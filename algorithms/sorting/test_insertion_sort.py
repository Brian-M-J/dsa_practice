import unittest
import insertion_sort as ins
from random import randint
from copy import deepcopy

class TestInsertionSorts(unittest.TestCase):
    def test_basic_insort(self):
        for i in range(0, 21):
            array = [randint(-50, 50) for _ in range(i)]
            sorted_array = ins.insertion_sort(array, inplace=False)
            self.assertEqual(sorted_array, sorted(array), msg=f'Test failed on instance:\n{array}\nwith output:\n{sorted_array}\n(inplace = False)')            
        for i in range(0, 21):
            array = [randint(-50, 50) for _ in range(i)]
            unsorted_array = deepcopy(array)
            ins.insertion_sort(array, inplace=True)
            self.assertEqual(array, sorted(unsorted_array), msg=f'Test failed on instance:\n{unsorted_array}\nwith output:\n{array}\n(inplace = True)')            

if __name__ == "__main__":
    unittest.main()

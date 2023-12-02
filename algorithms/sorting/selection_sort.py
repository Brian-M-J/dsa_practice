import unittest
import logging
from random import randint
from copy import deepcopy


def selection_sorted(user_list):
    user_list = deepcopy(user_list)
    for i, _ in enumerate(user_list[:-1]):
        logging.debug(f"{i = }")

        min_index = user_list.index(min(user_list[i + 1 :]), i + 1)
        logging.debug(f"{min_index = }, min element = {user_list[min_index]}")

        if user_list[i] > user_list[min_index]:
            user_list[min_index], user_list[i] = user_list[i], user_list[min_index]
        logging.debug(f"Swapping {user_list[min_index]} and {user_list[i]}")
        logging.debug(f"Elements after swapping: {user_list}")
    return user_list


class _TestSelectionSort(unittest.TestCase):
    def test_selection_sort(self):
        for i in range(51):
            test_list = [randint(0, 50) for _ in range(i)]
            logging.debug(f"Unsorted list: {test_list}")
            sorted_list = selection_sorted(test_list)
            logging.debug(f"Sorted list: {sorted_list}")
            self.assertEqual(
                sorted_list,
                list(sorted(test_list)),
                f"\nTest faied on case {test_list}\nWith output {sorted_list}",
            )


if __name__ == "__main__":
    if __debug__:
        logging.basicConfig(
            level=logging.DEBUG,
            style="{",
            format="{levelname} | {funcName} | {message}",
        )
    unittest.main()

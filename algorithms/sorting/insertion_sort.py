import unittest
import logging
from random import randint
from copy import deepcopy


def insertion_sorted(user_list):
    user_list = deepcopy(user_list)
    for i in range(1, len(user_list)):
        selected_index = i
        logging.debug(f"initial {selected_index = }")

        while (
            user_list[selected_index] < user_list[selected_index - 1]
            and selected_index > 0
        ):
            logging.debug(
                f"Swapping {user_list[selected_index]} and {user_list[selected_index - 1]}"
            )
            user_list[selected_index], user_list[selected_index - 1] = (
                user_list[selected_index - 1],
                user_list[selected_index],
            )
            logging.debug(
                f"Decreasing selected_index from {selected_index} to {selected_index - 1}"
            )
            selected_index -= 1

        logging.debug(f"{i = }, {user_list = }")
    return user_list


class _TestInsertionSort(unittest.TestCase):
    def test_insertion_sort(self):
        for i in range(51):
            test_list = [randint(0, 50) for _ in range(i)]
            logging.debug(f"Unsorted list: {test_list}")
            sorted_list = insertion_sorted(test_list)
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

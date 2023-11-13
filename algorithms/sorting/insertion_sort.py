from random import randint
from sys import argv, stderr, exit
from copy import deepcopy
from collections.abc import MutableSequence
import logging

def insertion_sort(array: MutableSequence, inplace=False) -> MutableSequence | None:
    '''
    Sorts a MutableSequence in ascending order.
    if inplace == False, a sorted copy is returned instead of modifying the passed MutableSequence
    '''
    if not inplace:
        array = deepcopy(array)
    for i in range(1, len(array) + 1):
        logging.debug(f'{i = }')
        for j in range(i - 1, 0, -1):
            logging.debug(f'{j = }')
            if array[j] < array[j - 1]:
                logging.debug(f'Swapping {array[j]} and {array[j - 1]}')
                array[j], array[j - 1] = array[j - 1], array[j]
        logging.debug(f'{array = }')
    if not inplace:
        return array
    else:
        return None

def get_array_from_user() -> list[int]:
    while True:
        try:
            user_input = input('Enter sequence of integers separated by spaces:\n>>> ')
            if user_input == '':
                return []
            array = map(int, user_input.split())
            return list(array)
        except ValueError:
            print('Inputs must be integers')
    
def main() -> None:
    array_length: int
    array: list[int]
    while True:
        choice = input('1 - Enter array manually\n2 - Randomly generate array\n3 - Exit\n>>> ')
        match choice:
            case '1':
                array = get_array_from_user()
                break
            case '2':
                array_length = randint(0, 20)
                array = [randint(-50, 50) for _ in range(array_length)]
                break
            case '3':
                exit()
            case wrong:
                print(f'Invalid input received: {wrong}')
    print(f'Unsorted array: {array}')
    while True:
        choice = input('1 - Sort in place\n2 - Do not sort in place\n3 - Exit\n>>> ')
        match choice:
            case '1':
                insertion_sort(array, inplace=True)
                break
            case '2':
                array = insertion_sort(array, inplace=False)
                break
            case '3':
                exit()
            case wrong:
                print(f'Invalid input received: {wrong}')
    print(f'Sorted array: {array}')
    

if __name__ == "__main__":
    if __debug__:
        logging.basicConfig(level=logging.DEBUG)
    main()

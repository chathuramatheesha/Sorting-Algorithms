from constants.settings import SUCCESS, FAIL, ALPHABET, SORTED_LIST
from typing import List

count = 0
result = ''


def check_in_sequence(list_one: List, list_two: List) -> bool:
    if len(list_one) != len(list_two):
        return False
    for x in range(len(list_one)):
        if list_one[x] != list_two[x]:
            return False
    return True


def test_sort(sorting_method: str, sorting_method_list: List):
    global result
    global count
    alphabet_letter = ALPHABET[count].upper()
    print(f'\nTest {alphabet_letter}: Check sorted list with {sorting_method} sort list')
    if check_in_sequence(SORTED_LIST, sorting_method_list):
        print(f'{SUCCESS}Selection Sort List: {sorting_method_list}')
        result += alphabet_letter
    else:
        print(f'{FAIL}List not sorted')
        print(f'Expected Output: {SORTED_LIST}')
        print(f'Actual Output: {sorting_method_list}')
        result += '-'
    count += 1


def get_results():
    global result
    return result

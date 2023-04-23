from sorting_algorithms.quick_sort import quick_sort
from sorting_algorithms.selection_sort import selection_sort
from typing import List


def check_in_sequence(list_one: List, list_two: List) -> bool:
    for x in range(len(list_one)):
        if list_one[x] != list_two[x]:
            return False
    return True


if __name__ == '__main__':
    SUCCESS = 'SUCCESS::'
    FAIL = 'FAIL::'

    my_list = [26, 12, 23, 10, 24, 27, 29]
    sorted_list = [10, 12, 23, 24, 26, 27, 29]
    result = ''

    # Test A Check created list with sorted list
    print('\nTest A: Check created list with created list')
    if not check_in_sequence(my_list, sorted_list):
        print(f'{SUCCESS}')
        print(f'Original List: {my_list}')
        print(f'Sorted List: {sorted_list}')
        result += 'A'
    else:
        print(f'{FAIL}Problem with check in sequence function')
        result += '-'

    # Test B Check list with quick sort list
    print('\nTest B: Check created list with quick sort list')
    if check_in_sequence(sorted_list, quick_sort(my_list)):
        print(f'{SUCCESS}Quick Sort List: {my_list}')
        result += 'B'
    else:
        print(f'{FAIL}List not sorted')
        print(f'Expected Output: {sorted_list}')
        print(f'Actual Output: {quick_sort(my_list)}')
        result += '-'

    # Test C Check list with selection sort list
    print('\nTest C: Check created list with selection sort list')
    if check_in_sequence(sorted_list, selection_sort(my_list)):
        print(f'{SUCCESS}Selection Sort List: {my_list}')
        result += 'C'
    else:
        print(f'{FAIL}List not sorted')
        print(f'Expected Output: {sorted_list}')
        print(f'Actual Output: {selection_sort(my_list)}')
        result += '-'

    # Display Summary of the results
    print('\n\n------------------------------------ SUMMARY ------------------------------------')
    print('Tests passed: ', result)

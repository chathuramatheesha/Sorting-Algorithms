from utils import test_sort, get_results
from sorting_algorithms.selection_sort import selection_sort
from sorting_algorithms.bubble_sort import bubble_sort
from sorting_algorithms.quick_sort import quick_sort

from constants.settings import MY_LIST

if __name__ == '__main__':
    # Test A sorted list with Selection sort list
    test_sort('Selection', selection_sort(MY_LIST))

    # Test B sorted list with Bubble sort list
    test_sort('Bubble', bubble_sort(MY_LIST))

    # Test C sorted list with Insertion sort list
    # test_sort('Insertion', insertion_sort(MY_LIST))

    # Test D sorted list with Merge sort list
    # test_sort('Merge', merge_sort(MY_LIST))

    # Test E sorted list with Quick sort list
    test_sort('Quick', quick_sort(MY_LIST))

    # Display Summary of the results
    print('\n\n------------------------------------ SUMMARY ------------------------------------')
    print('Tests passed: ', get_results())

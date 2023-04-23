from typing import List


# Quick Sort with List Comprehensions
def quick_sort(sorting_list):
    if len(sorting_list) <= 1:
        return sorting_list
    else:
        pivot = sorting_list[0]
        left = [x for x in sorting_list[1:] if x < pivot]
        right = [x for x in sorting_list[1:] if x >= pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)


def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1


def quick_sort_partition(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quick_sort_partition(array, low, pi - 1)
        quick_sort_partition(array, pi + 1, high)
    else:
        return array

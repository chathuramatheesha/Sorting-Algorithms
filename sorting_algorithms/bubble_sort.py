from typing import List


def bubble_sort(sorting_list: List) -> List:
    sorted_list = sorting_list.copy()
    list_size = len(sorted_list) - 1
    for x in range(list_size):
        for y in range(list_size - x):
            if sorted_list[y] > sorted_list[y + 1]:
                temp = sorted_list[y]
                sorted_list[y] = sorted_list[y + 1]
                sorted_list[y + 1] = temp
    return sorted_list

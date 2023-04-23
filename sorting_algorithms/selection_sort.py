from typing import List


def selection_sort(sorting_list: List) -> List:
    sorted_list = sorting_list.copy()
    list_size = len(sorted_list)
    min_index = 0
    for x in range(1, list_size):
        for y in range(x, list_size):
            if sorted_list[y] < sorted_list[min_index]:
                temp = sorted_list[x - 1]
                sorted_list[x - 1] = sorted_list[y]
                sorted_list[y] = temp
        min_index = x
    return sorted_list

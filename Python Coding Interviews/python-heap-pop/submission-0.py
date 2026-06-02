import heapq
from typing import List


def heap_pop(heap: List[int]) -> List[int]:
    # pops all elements from heap
    # return them in a list in the order that they were
    # popped

    new_list = []

    list_len = len(heap)

    for i in range(list_len):
        new_list.append(heapq.heappop(heap))

    return new_list


# do not modify below this line
print(heap_pop([1, 2, 3]))
print(heap_pop([1, 3, 2]))
print(heap_pop([6, 7, 8, 12, 9, 10]))

import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    # makes list with numbers in reverse order

    my_heap = []

    reverse_list = []

    for num in nums:
        pair = (-num,num)
        heapq.heappush(my_heap, pair)

    # now we need to use heappop

    while my_heap:
        the_tuple = heapq.heappop(my_heap)
        reverse_list.append(the_tuple[1])

    return reverse_list



# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))

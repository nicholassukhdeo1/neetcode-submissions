import heapq
from typing import List


def get_min_element(arr: List[int]) -> int:
    

    return min(arr)


def get_min_4_elements(arr: List[int]) -> List[int]:
    # Return elements in *increasing* order

    # thats basic heap implementation


    return heapq.nsmallest(4, arr)


def get_min_2_elements(arr: List[int]) -> List[int]:
    # Return elements in *decreasing* order

    # this is doing the custom max heap?
    # or just 

    my_list = heapq.nsmallest(2, arr) #1,2

    temp = my_list[0]
    my_list[0] = my_list[1]
    my_list[1] = temp

    return my_list


# do not modify below this line
print(get_min_element([1, 2, 3]))
print(get_min_element([3, 2, 1, 4, 6, 2]))
print(get_min_element([1, 9, 7, 3, 2, 1, 4, 6, 2]))

print(get_min_4_elements([1, 9, 7, 3, 2, 1, 4, 6, 2]))
print(get_min_4_elements([1, 9, 7, 2, 1, 3, 2, 1, 4, 6, 2, 1]))
print(get_min_4_elements([1, 9, 7, 2, 3, 2, 4, 6, 2]))

print(get_min_2_elements([1, 9, 7, 3, 2, 1, 4, 6, 2]))
print(get_min_2_elements([1, 9, 7, 2, 1, 3, 2, 1, 4, 6, 2, 1]))
print(get_min_2_elements([1, 9, 7, 2, 3, 2, 4, 6, 2]))


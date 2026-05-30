from typing import List


def reverse_list(arr: List[int]) -> List[int]:
    pass
    # use [-1]

    arr_length = len(arr)
    new_list = []

    for i in range(arr_length):
        new_list.append(arr[-1])
        arr.pop()

    return new_list
        


# do not modify below this line
print(reverse_list([1, 2, 3]))
print(reverse_list([3, 2, 1, 4, 6, 2]))
print(reverse_list([1, 9, 7, 3, 2, 1, 4, 6, 2]))

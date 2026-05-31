from typing import List, Dict


def num_to_index(nums: List[int]) -> Dict[int, int]:
    # returns a dict where its keys are the elements
    # in the list

    # my_dict = {}

    # for index, number in enumerate(nums):
    #     my_dict[number] = index

    my_dict = {number: index for index, number in enumerate(nums)}

    return my_dict





# do not modify below this line
print(num_to_index([1, 2, 3, 4, 5, 6, 7, 8]))
print(num_to_index([8, 7, 6, 5, 4, 3, 2, 1]))
print(num_to_index([0, 3, 2, 4, 5, 1]))

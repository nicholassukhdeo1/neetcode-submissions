from typing import List


def get_index_of_seven(nums: List[int]) -> int:
    #returns first occurrence of 7

    for index, number in enumerate(nums):
        if nums[index] == 7:
            return index


    return -1

def get_dist_between_sevens(nums: List[int]) -> int:
    pass

    occurrence_count = 0

    for index, number in enumerate(nums):
        if nums[index] == 7 and occurrence_count == 0:
            first_seven = index
            occurrence_count += 1
        elif nums[index] == 7 and occurrence_count == 1:
            second_seven = index
            return second_seven - first_seven


# do not modify below this line
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 8, 9]))
print(get_index_of_seven([2, 4, 7, 5, 7, 8, 4, 2]))

print(get_dist_between_sevens([1, 2, 7, 4, 5, 6, 7, 8, 9]))
print(get_dist_between_sevens([2, 7, 7, 7, 8]))
print(get_dist_between_sevens([7, 4, 8, 4, 2, 7]))

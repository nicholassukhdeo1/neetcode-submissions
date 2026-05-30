from typing import List


def disallow_negatives(num: int) -> int:
    #returns int if it is greater than 0

    is_negative = max(0, num)


    return is_negative


def max_difference(nums: List[int]) -> int:
    
    #returns the max difference between two
    #numbers in a list that r right next to each other

    arr_length = len(nums)

    maxDiff = -1

    # if maxDiff < currDiff
    # make maxDiff equal to currDiff

    i = 1

    for i in range(arr_length):
        currDiff = nums[i] - nums[i-1]

        maxDiff = max(currDiff, maxDiff)

    return maxDiff




# do not modify below this line
print(disallow_negatives(-2))
print(disallow_negatives(-1))
print(disallow_negatives(0))
print(disallow_negatives(1))
print(disallow_negatives(2))

print(max_difference([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(max_difference([1, 2, 3, 4, 5, 6, 8, 9]))
print(max_difference([10, 1, 3, 7]))
print(max_difference([2, 4, 7, 5, 7, 8, 4, 2]))

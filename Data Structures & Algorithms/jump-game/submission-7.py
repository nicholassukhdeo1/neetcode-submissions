class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # keep track of furthest array

        # if furthest array == size-1, return true

        furthest = 0

        size = len(nums)

        if size == 1:
            return True


        for index in range(size):
            if furthest < index:
                return False

            cur_furthest = index + nums[index]

            furthest = max(furthest,cur_furthest)

            if furthest >= (size-1):
                return True



        return False
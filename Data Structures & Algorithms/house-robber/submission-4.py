class Solution:
    def rob(self, nums: List[int]) -> int:
        
        size = len(nums)

        cache = [-1] * size

        def helper(index):
            if index > size-1:
                return 0
            if cache[index] != -1:
                return cache[index]


            cache[index] = max(nums[index] + helper(index+2),helper(index+1))

            return cache[index]

        return helper(0)
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        size = len(nums)
        res = 0

        cache = {}

        def memoization(index):
            if index > size-1:
                return 0

            if index in cache:
                return cache[index]
                

            cache[index] = max(nums[index] + memoization(index+2), memoization(index+1))

            return cache[index]

            

        for index in range(size):
            res = max(res,memoization(index))

        return res
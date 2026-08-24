class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # first and last house are neighbors.

        if len(nums) == 1:
            return nums[0]
        
        cache = {}

        size = len(nums)
        
        def memoization(index,end,cache):
            
            if index >= end:
                return 0
            if index in cache:
                return cache[index]


            cache[index] = max(nums[index] + memoization(index+2,end,cache),memoization(index+1,end,cache))     
            

            return cache[index]


        return max(memoization(0,size-1,{}),memoization(1,size,{}))
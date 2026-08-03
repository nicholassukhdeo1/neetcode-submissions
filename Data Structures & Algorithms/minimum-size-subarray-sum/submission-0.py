class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        L = 0
        length = len(nums) + 1
        sum = 0


        for R in range(len(nums)):
            sum += nums[R]
            while sum >= target:
                length = min(R-L+1,length)
                sum -= nums[L]
                L += 1


        if length > len(nums):
            return 0
        return length

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        
        if len(nums) == 1:
            return nums[0]
        
        curSum = float('-inf')

        maxSum = float('-inf')
        

        for num in nums:
            if num > curSum and curSum < 0:
                curSum = num
            else:
                curSum += num

            maxSum = max(maxSum,curSum)



        return maxSum
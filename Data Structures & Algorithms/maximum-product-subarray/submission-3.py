class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMax, curMin = 1,1

        for number in nums:
            if number == 0:
                curMax, curMin = 1,1
                continue
            
            temp = curMax * number
            curMax = max(number,temp,curMin*number)
            curMin = min(number,temp,curMin*number)

            res = max(res,curMax)


        return res
        
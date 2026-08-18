class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []

        curCombo = []
        
        def helper(res,curCombo,start,curSum):

            if curSum == target:
                res.append(curCombo.copy())
                return
            if curSum > target:
                return


            # basically, if we've already found combos for all numbers provided, stop!
            if start >= len(nums):
                return

            for i in range(start,len(nums)):
                curSum += nums[i]
                curCombo.append(nums[i])
                helper(res,curCombo,i,curSum)
                subtract = curCombo.pop()
                curSum -= subtract


        helper(res,curCombo,0,0)

        return res
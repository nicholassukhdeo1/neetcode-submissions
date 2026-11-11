class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        

        numberCheck = set()

        for i in range(len(nums)):

            candidate = nums[i]

            if candidate in numberCheck:
                return candidate

            numberCheck.add(candidate)
    

            
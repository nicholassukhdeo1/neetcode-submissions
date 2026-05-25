class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

      
        # you already have ur names

        numberMap = {}

        for number in nums:

            if number not in numberMap:

                numberMap[number] = 1

            else:

                numberMap[number] += 1
                return True

        return False
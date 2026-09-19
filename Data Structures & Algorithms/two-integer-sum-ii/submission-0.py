class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # they add up to target

        # and the index1 is < than index2
        
        # index1 != index2

        L = 0
        R = len(numbers) - 1

        curr_sum = 0

        res = []

        while L < R:
            curr_sum = numbers[L] + numbers[R]

            if target > curr_sum:
                L += 1
            elif target < curr_sum:
                R -= 1
            else:
                res.append(L+1)
                res.append(R+1)
                return res

        return res
                
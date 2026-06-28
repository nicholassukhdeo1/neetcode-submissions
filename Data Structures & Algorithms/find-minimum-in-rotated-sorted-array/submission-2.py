class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        #start ptrs on either end


        #at leftmost end
        res = nums[0]

        L = 0
        R = len(nums) - 1


        #you want to think about this 

        while L <= R:
            
            #guarantees that the section that we're looking at is sorted.
            # because ur leftmost chunk is smaller than rightmost.
            if nums[L] < nums[R]:
                res = min(res, nums[L])
                break

            M = (L + R) // 2
            res = min(res, nums[M])


            if nums[M] >= nums[L]:
                L = M + 1
            else:
                R = M - 1

        return res


            
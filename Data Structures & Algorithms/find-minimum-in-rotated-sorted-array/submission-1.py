class Solution:
    def findMin(self, nums: List[int]) -> int:
        

        # looking for pibot point where sorted order
        # breaks

        #find the point where the next number isnt bigger
        # that IS the min

        L = 0
        R = len(nums) - 1

        while L < R:
            mid = (L+R) // 2

            if nums[R] > nums[mid]:
                R = mid

            elif nums[R] < nums[mid]:
                L = mid+1
            

        return nums[L]

        # what if i use a helper function

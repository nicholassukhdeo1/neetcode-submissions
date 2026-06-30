class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) - 1

        while L<= R:

            mid = (L+R) // 2
            if nums[mid] == target:
                return mid
            
            #left sort portion

            if nums[mid] >= nums[L]:
                if target > nums[mid]:
                    L = mid+1
                elif target < nums[L]:
                    L = mid+1
                else:
                    R = mid-1
            else:
                if target < nums[mid]:
                    R = mid-1
                elif target > nums[R]:
                    R = mid-1
                else:
                    L = mid+1

        return -1
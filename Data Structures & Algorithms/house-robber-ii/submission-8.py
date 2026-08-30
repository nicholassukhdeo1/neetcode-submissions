class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        size = len(nums)-1

        # cache = [-1] * size

        nums1 = (nums[1:]).copy()

        nums2 = (nums[:-1]).copy()

        





        def helper(index,nums,cache):
            if index > size-1:
                return 0
            if index in cache:
                return cache[index]


            cache[index] = max(nums[index] + helper(index+2,nums,cache),helper(index+1,nums,cache))

            return cache[index]

        return max(helper(0,nums1,{}),helper(0,nums2,{}))
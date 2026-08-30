class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:


        size = len(nums)

        memo = [-1] * size

        def dfs(i):
            if memo[i] != -1:
                return memo[i]


            LIS = 1

            
            for j in range(i+1,size):
                if nums[i] < nums[j]:
                    LIS = max(LIS, 1 + dfs(j))


            memo[i] = LIS


            return LIS

        return max(dfs(i) for i in range(size))

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        

        cache = {}
        size = len(cost)


        def dfs(index):

            if index >= size:
                return 0

            if index in cache:
                return cache[index]

            cache[index] = cost[index] + min(dfs(index+1),dfs(index+2))

            return cache[index]

        return min(dfs(0),dfs(1))
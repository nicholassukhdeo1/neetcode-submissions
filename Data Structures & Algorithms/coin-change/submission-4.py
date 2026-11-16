class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        cache = {}

        def dfs(curr_sum):

            if curr_sum > amount:
                return float('inf')
            if curr_sum == amount:
                return 0
            if curr_sum in cache:
                return cache[curr_sum]
            
            best = float('inf')

            for c in coins:
                best = min(best,1 + dfs(c + curr_sum))

            cache[curr_sum] = best

            return best

        res = dfs(0)
        if res == float('inf'):
            return -1
        else:
            return res
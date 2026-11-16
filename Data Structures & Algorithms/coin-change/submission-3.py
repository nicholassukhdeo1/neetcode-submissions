class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}

        # fewest coins needed to go from `total` up to `amount`
        def dfs(total):
            if total > amount:
                return float('inf')
            if total == amount:
                return 0
            if total in cache:
                return cache[total]

            best = float('inf')
            for c in coins:
                best = min(best, 1 + dfs(total + c))

            cache[total] = best
            return best

        res = dfs(0)
        return -1 if res == float('inf') else res
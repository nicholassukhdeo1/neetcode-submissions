class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        L = 0

        size = len(prices)

        res = float('-inf')

        for R in range(size):
            profit = prices[R] - prices[L]

            if prices[L] > prices[R]:
                L = R


            res = max(res, profit)


        return res



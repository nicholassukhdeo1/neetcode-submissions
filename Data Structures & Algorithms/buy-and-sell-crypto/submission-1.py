class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_profit = 0
        L = 0
        
        for R in range(1,len(prices)):
            diff = prices[R] - prices[L]
            if diff > curr_profit:
                curr_profit = diff

            if prices[R] < prices[L]:
                # L += 1
                L = R

        return curr_profit
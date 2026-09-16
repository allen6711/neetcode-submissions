class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_diff = 0
        n = len(prices)
        for i in range(n):
            for j in range(i + 1, n):
                if prices[j] - prices[i] > max_diff:
                    max_diff = prices[j] - prices[i]
        
        return max_diff
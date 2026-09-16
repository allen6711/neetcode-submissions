class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        
        return max_profit

        max_diff = 0
        n = len(prices)
        for i in range(n):
            for j in range(i + 1, n):
                if prices[j] - prices[i] > max_diff:
                    max_diff = prices[j] - prices[i]
        
        return max_diff
